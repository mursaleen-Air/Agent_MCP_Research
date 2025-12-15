from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

# create agents
memory = MemoryAgent()
research = ResearchAgent(knowledge_base)
analysis = AnalysisAgent()

# give agents to coordinator
manager = Coordinator(research, analysis, memory)

# start system
manager.handle_query(user_input)
