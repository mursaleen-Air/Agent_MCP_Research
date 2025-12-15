# d:\Mursaleen\Mursaleen\5th semester\knowledge Representation and Reasoning\A3\agents\research_agent.py

class ResearchAgent:
    def __init__(self, knowledge_base):
        """
        Initialize the ResearchAgent with a knowledge base (e.g., a dictionary).
        """
        self.knowledge_base = knowledge_base

    def research(self, topic):
        """
        Look up the given topic in the knowledge base. 
        Returns relevant information, or a message if the topic isn't known.
        """
        info = self.knowledge_base.get(topic.lower())
        if info:
            return info
        else:
            return f"Sorry, I couldn't find information about '{topic}'."