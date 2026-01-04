"""
Podcast Application - Console Interface
Creates podcast scripts based on user topics using a workflow with search and script generation agents.
"""

import asyncio
import sys
import time
from agent_framework import (
    WorkflowOutputEvent,
    RequestInfoEvent,
    AgentRunUpdateEvent,
    WorkflowStatusEvent,
    WorkflowRunState,
)
from workflow import workflow, ScriptApprovalRequest


# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def show_loading(message="Processing"):
    """Show a loading indicator."""
    sys.stdout.write(f"{Colors.YELLOW}{message}... {Colors.RESET}")
    sys.stdout.flush()


def clear_loading():
    """Clear the loading indicator."""
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()


async def main():
    """Run the podcast workflow application."""
    print("=" * 60)
    print("Welcome to Podcast Application")
    print("=" * 60)
    print()
    
    # Get topic from user
    topic = input("Please give topic: ").strip()
    if not topic:
        print("No topic provided. Exiting...")
        return
    
    print(f"\nStarting workflow for topic: {topic}")
    print("-" * 60)
    
    # Track current agent and final script
    current_agent = None
    final_script = None
    pending_requests = {}
    loading_shown = False
    
    # Start workflow
    workflow_complete = False
    pending_responses = None
    
    while not workflow_complete:
        # Run or continue workflow
        if pending_responses:
            stream = workflow.send_responses_streaming(pending_responses)
        else:
            stream = workflow.run_stream(topic)
        
        pending_responses = None
        
        # Process events
        async for event in stream:
            # Agent response updates
            if isinstance(event, AgentRunUpdateEvent):
                # Get agent name from executor_id
                agent_name = event.executor_id
                
                # Print agent name header when agent changes
                if agent_name != current_agent:
                    # Clear loading indicator if shown
                    if loading_shown:
                        clear_loading()
                        loading_shown = False
                    
                    current_agent = agent_name
                    print(f"\n{Colors.BOLD}[{agent_name.upper()}]:{Colors.RESET}")
                    
                    # Show loading before first output
                    if not event.data or not event.data.text:
                        show_loading(f"Waiting for {agent_name}")
                        loading_shown = True
                
                # Print agent response text in green
                if event.data and event.data.text:
                    # Clear loading if shown
                    if loading_shown:
                        clear_loading()
                        loading_shown = False
                    
                    print(f"{Colors.GREEN}{event.data.text}{Colors.RESET}", end="", flush=True)
            
            # Human approval request
            elif isinstance(event, RequestInfoEvent):
                if isinstance(event.data, ScriptApprovalRequest):
                    # Clear loading if shown
                    if loading_shown:
                        clear_loading()
                        loading_shown = False
                    
                    print("\n")
                    print("-" * 60)
                    print(f"{Colors.CYAN}{Colors.BOLD}REVIEW REQUIRED{Colors.RESET}")
                    print("-" * 60)
                    print(f"{Colors.GREEN}Generated Script:\n{event.data.generated_script}{Colors.RESET}")
                    print("-" * 60)
                    print(f"{Colors.YELLOW}{event.data.prompt}{Colors.RESET}")
                    
                    # Get user input
                    user_response = input(f"{Colors.CYAN}Your response: {Colors.RESET}").strip()
                    pending_responses = {event.request_id: user_response}
                    
                    # If approved, save the script for later
                    if user_response in ["Yes", "yes"]:
                        final_script = event.data.generated_script
                    
                    print(f"\n{Colors.YELLOW}Continuing workflow...{Colors.RESET}")
                    # Show loading for next step
                    show_loading("Processing")
                    loading_shown = True
            
            # Workflow output (final)
            elif isinstance(event, WorkflowOutputEvent):
                # Clear loading if shown
                if loading_shown:
                    clear_loading()
                    loading_shown = False
                
                print("\n")
                print("=" * 60)
                print(f"{Colors.BOLD}{Colors.GREEN}WORKFLOW COMPLETE{Colors.RESET}")
                print("=" * 60)
                
                # Save to file
                if final_script:
                    output_file = "podcast.txt"
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(final_script)
                    print(f"\n{Colors.GREEN}✓ Script saved to {output_file}{Colors.RESET}")
                    print(f"\n{Colors.GREEN}{event.data}{Colors.RESET}")
                
                workflow_complete = True
            
            # Workflow status changes
            elif isinstance(event, WorkflowStatusEvent):
                if event.state == WorkflowRunState.IDLE:
                    if not any(isinstance(e, WorkflowOutputEvent) for e in [event]):
                        workflow_complete = True
    
    print("\nThank you for using Podcast Application!")


if __name__ == "__main__":
    asyncio.run(main())
