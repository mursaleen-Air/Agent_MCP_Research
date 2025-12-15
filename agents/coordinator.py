import datetime


class Coordinator:
    def __init__(self, research_agent, analysis_agent, memory_agent):
        self.research_agent = research_agent
        self.analysis_agent = analysis_agent
        self.memory_agent = memory_agent

        # simple system state
        self.conversation_id = 0

    def classify_query(self, user_query):
        """
        Decide what kind of query this is.
        This is a very simple planner (rule-based).
        """

        query = user_query.lower()

        # memory-related queries
        if "what did we discuss" in query or "earlier" in query or "remember" in query:
            return "memory"

        # analysis-heavy queries
        if "compare" in query or "analyze" in query or "which is better" in query:
            return "analysis"

        # default: research
        return "research"

    def handle_query(self, user_query):
        """
        Main orchestration method.
        """

        self.conversation_id += 1
        timestamp = datetime.datetime.now().isoformat()

        print(f"\n[Coordinator] New Query Received: {user_query}")
        print(f"[Coordinator] Conversation ID: {self.conversation_id}")

        # Step 1: classify query
        query_type = self.classify_query(user_query)
        print(f"[Coordinator] Query classified as: {query_type}")

        # Step 2: check memory first (avoid redundant work)
        memory_hit = self.memory_agent.search(user_query)
        if memory_hit:
            print("[Coordinator] Found relevant information in memory.")
            return self.synthesize_response(memory_hit)

        # Step 3: route task to appropriate agent
        if query_type == "research":
            print("[Coordinator] Routing task to ResearchAgent")
            result = self.research_agent.handle(user_query)

        elif query_type == "analysis":
            print("[Coordinator] Routing task to ResearchAgent first (dependency)")
            research_data = self.research_agent.handle(user_query)

            print("[Coordinator] Routing task to AnalysisAgent")
            result = self.analysis_agent.handle(user_query, research_data)

        elif query_type == "memory":
            print("[Coordinator] Routing task to MemoryAgent")
            result = self.memory_agent.handle(user_query)

        else:
            result = "I am not sure how to handle this query."

        # Step 4: store result in memory
        self.memory_agent.store({
            "conversation_id": self.conversation_id,
            "timestamp": timestamp,
            "query": user_query,
            "result": result,
            "handled_by": query_type,
            "confidence": 0.85
        })

        # Step 5: return final answer
        return self.synthesize_response(result)

    def synthesize_response(self, results):
        """
        Convert agent output into a user-friendly response.
        """
        print("[Coordinator] Synthesizing final response\n")
        return str(results)
