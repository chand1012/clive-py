from smolagents import CodeAgent
from src.agents.models import llm_model


agent = CodeAgent(tools=[], model=llm_model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
