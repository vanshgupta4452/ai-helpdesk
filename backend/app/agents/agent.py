from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

def create_ticket_tool(input_text):
    return f"Ticket created for: {input_text}"

tools = [
    Tool(
        name="CreateTicket",
        func=create_ticket_tool,
        description="Create a support ticket"
    )
]

llm = OpenAI(temperature=0)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

def run_agent(query):
    return agent.run(query)