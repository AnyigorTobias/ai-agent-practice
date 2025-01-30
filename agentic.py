from phi.agent import Agent
from phi.model.groq import Groq
from knowledge_base import knowledge_base

from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    knowledge=knowledge_base,
    search_knowledge=True,
)
agent.knowledge.load(recreate=False)

agent.print_response("What are the top opportunities for an engineering graduate with a 2.1 degree and under 27 years old?")
