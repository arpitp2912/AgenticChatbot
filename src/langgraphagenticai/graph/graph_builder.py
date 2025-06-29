from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import START, END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    """
    A class to build a graph structure for LangGraph Agentic AI.
    This class is responsible for constructing the graph based on the provided nodes and edges.
    """

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_graph(self):
        """
        Builds a basic chatbot graph structure.
        This method sets up the graph with a single node for the chatbot.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase):
        """
        Sets up the graph based on the selected use case.
        This method initializes the graph structure for the specified use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_graph()

        return self.graph_builder.compile()
