from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot node that can be used in a LangGraph workflow.
    This node can be used to create a simple chatbot that responds to user input.
    """

    def __init__(self, model: str):
        self.llm = model

    def process(self, state:State)-> dict:
        """
        Process the user input and generate a response using the LLM.
        """
        return {"messages": self.llm.invoke(state["messages"])}