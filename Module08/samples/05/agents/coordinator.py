import json
from .specialists import RetrievalAgent, ReasoningAgent, ExecutionAgent

class Coordinator:
    def __init__(self):
        self.retrieval = RetrievalAgent()
        self.reasoning = ReasoningAgent()
        self.execution = ExecutionAgent()

    def handle(self, user_goal: str) -> dict:
        context = self.retrieval.run(user_goal)
        decision = self.reasoning.run(context, user_goal)
        actions = self.execution.run(decision)
        return {
            "goal": user_goal,
            "context": context,
            "decision": decision,
            "actions": actions
        }

if __name__ == "__main__":
    # Ensure: foundry model run phi-4-mini
    coord = Coordinator()
    result = coord.handle("Create a plan to onboard 5 new customers this month")
    print(json.dumps(result, indent=2))
