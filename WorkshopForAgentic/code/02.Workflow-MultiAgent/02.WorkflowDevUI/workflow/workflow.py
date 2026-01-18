from dataclasses import dataclass
from agent_framework import (
    WorkflowBuilder,
    WorkflowContext,
    Executor,
    AgentExecutorResponse,
    AgentExecutorRequest,
    ChatMessage,
    Role,
    handler,
    response_handler,
    AgentExecutor,
)
from search_agent import setup_search_agent
from generate_script_agent import setup_gen_script_agent


@dataclass
class ScriptApprovalRequest:
    """Request for user to approve or reject the generated script."""
    prompt: str
    generated_script: str


class ReviewExecutor(Executor):
    """Executor that requests user approval and handles the response."""

    def __init__(self, id: str, genscript_agent_id: str):
        super().__init__(id=id)
        self._genscript_agent_id = genscript_agent_id

    @handler
    async def review_script(self, response: AgentExecutorResponse, ctx: WorkflowContext) -> None:
        """Handle the generated script from genscriptagent and request approval."""
        # Extract the generated script text
        script_text = response.agent_response.text

        # Request user approval
        await ctx.request_info(
            request_data=ScriptApprovalRequest(
                prompt="Do you accept this script? Type 'Yes' or 'yes' to accept, anything else to regenerate.",
                generated_script=script_text
            ),
            response_type=str,
        )

    @response_handler
    async def handle_approval_response(
        self,
        original_request: ScriptApprovalRequest,
        response: str,
        ctx: WorkflowContext[AgentExecutorRequest],
    ) -> None:
        """Handle user's approval response."""
        user_input = response.strip()

        # Check if user approved
        if user_input in ["Yes", "yes"]:
            # User approved - end the workflow
            await ctx.yield_output(f"Script approved! Final script:\n{original_request.generated_script}")
        else:
            # User did not approve - send message back to genscriptagent to regenerate
            # Create feedback message and send as AgentExecutorRequest
            feedback_message = ChatMessage(
                role=Role.USER,
                text=f"The previous script was not accepted. User feedback: {user_input}. Please regenerate the script based on this feedback."
            )
            await ctx.send_message(
                AgentExecutorRequest(messages=[feedback_message], should_respond=True),
                target_id=self._genscript_agent_id
            )


# Setup agents - wrap with AgentExecutor for proper message handling
search_agent = setup_search_agent()
gen_script_agent = setup_gen_script_agent()

search_executor = AgentExecutor(agent=search_agent, id="search_executor")
gen_script_executor = AgentExecutor(agent=gen_script_agent, id="gen_script_executor")
review_executor = ReviewExecutor(id="review_executor", genscript_agent_id="gen_script_executor")

# Build workflow with approval loop
# search_executor -> gen_script_executor -> review_executor
# If not approved, review_executor -> gen_script_executor (loop back)
workflow = (
    WorkflowBuilder()
    .set_start_executor(search_executor)
    .add_edge(search_executor, gen_script_executor)
    .add_edge(gen_script_executor, review_executor)
    .add_edge(review_executor, gen_script_executor)  # Loop back for regeneration
    .build()
)