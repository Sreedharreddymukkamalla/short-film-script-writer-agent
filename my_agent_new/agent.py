from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

root_agent = Agent(
    model='gemini-2.5-flash',
    name='short_film_script_writer',
    description='The agent writes script for the short film based on the premise provided by the user.',
    instruction="""
        The agent writes script for the short film based on the premise provided by the user. The script should be professional and also 2 pages.
    """,
)
