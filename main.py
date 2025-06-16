import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
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
    async with stdio_client(stdio_server_parameters) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session initialized")
            tools = await load_mcp_tools(session)
            print(tools)

            agent = create_react_agent(llm, tools)
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 2 + 2?")]})
            print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
