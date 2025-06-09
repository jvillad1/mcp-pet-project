import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

# Debug: Check if API key is loaded
api_key = os.environ.get("OPENAI_API_KEY")
if api_key:
    print(f"✅ API key loaded successfully (length: {len(api_key)})")
    llm = ChatOpenAI(api_key=api_key)
else:
    print("❌ OPENAI_API_KEY not found in environment variables")
    print("Make sure you have a .env file with OPENAI_API_KEY=your_key")
    # You can uncomment the line below to exit if no API key is found
    # exit(1)
    llm = None

stdio_server_parameters = StdioServerParameters(
    command="python",
    args=["/Users/jvillada/Developer/mcp-servers/mcp-pet-project/servers/math_server.py"],
)

async def main():
    print("Hello from mcp-pet-project!")

if __name__ == "__main__":
    asyncio.run(main())
