# d:\Mursaleen\Mursaleen\5th semester\knowledge Representation and Reasoning\A3\agents\memory_agent.py

class AnalysisAgent:
    def analyze(self, data, question):
        """
        Analyzes the provided data based on the user's question.
        
        :param data: The data to analyze (could be a list, dict, etc.)
        :param question: The question specifying what to analyze.
        :return: Analysis result as a string.
        """
        # Basic example logic: respond based on question keyword
        question = question.lower()
        if "average" in question or "mean" in question:
            if isinstance(data, list) and data:
                avg = sum(data) / len(data)
                return f"The average is {avg:.2f}."
            else:
                return "Unable to calculate average: data is not a list of numbers."
        elif "max" in question or "highest" in question:
            if isinstance(data, list) and data:
                return f"The maximum value is {max(data)}."
            else:
                return "Unable to find maximum: data is not a list of numbers."
        elif "min" in question or "lowest" in question:
            if isinstance(data, list) and data:
                return f"The minimum value is {min(data)}."
            else:
                return "Unable to find minimum: data is not a list of numbers."
        else:
            return "I'm not sure how to analyze that question."