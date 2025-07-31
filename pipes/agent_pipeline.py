from typing import List, Union, Generator, Iterator
from schemas import OpenAIChatMessage
from pydantic import BaseModel
import os
import requests

# Get the MCP URL from environment variables, with a fallback for local development
MCP_URL = os.environ.get("MCP_URL", "http://mcpo:8000")

class Pipeline:
    """
    This pipeline implements a ReAct (Reasoning and Acting) agent.
    It uses a loop to think, act, and observe until it can provide a final answer.
    """

    class Valves(BaseModel):
        # Pass any configuration values here
        pass

    def __init__(self):
        self.id = "agent_pipeline"
        self.name = "Agent Pipeline"

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        """
        The main logic of the agent.
        """
        print(f"Pipe - Agent Pipeline: Received message '{user_message}'")

        system_prompt = """
        You are a helpful assistant that thinks step by step to solve problems.
        You have access to the following tools:

        - `search(query: str)`: Use this to search for information on the web.

        To use a tool, respond with a JSON object like this:
        {"thought": "I need to search for information about X.", "tool": "search", "tool_input": "X"}

        When you have enough information to answer, respond with:
        {"thought": "I have the answer.", "final_answer": "The final answer is..."}
        """

        # For simplicity, this example doesn't implement the full ReAct loop yet.
        # It will be expanded to include thinking, tool use, and delegation.

        # Placeholder for the ReAct loop logic
        # 1. Add system prompt to messages
        # 2. Call the LLM
        # 3. Parse the response for thought/action
        # 4. If action, execute it (e.g., call MCP)
        # 5. Append observation and repeat
        # 6. If final answer, return it

        # For now, let's return a simple response demonstrating it's working.
        return f"Agent Pipeline is active. I will process: '{user_message}' using the ReAct framework."

    def search_tool(self, query: str) -> str:
        """
        A placeholder for a tool that would query the MCP service.
        """
        print(f"Tool - Search: Querying MCP for '{query}'")
        try:
            # This is where you would construct the actual MCP request
            # For example, to use a hypothetical 'web_search' tool from MCP:
            response = requests.post(
                f"{MCP_URL}/tools/web_search",
                json={"query": query}
            )
            response.raise_for_status() # Raise an exception for bad status codes
            return response.json().get("result", "No result found.")
        except requests.exceptions.RequestException as e:
            print(f"Error calling MCP: {e}")
            return f"Error: Could not connect to the search tool."

