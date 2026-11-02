import asyncio
from uuid import uuid4

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
mcp_adapter=MCPAdapter("http://127.0.0.1:8000/mcp")

async def main():
    async with mcp_adapter:
        tool= await mcp_adapter.list_tools()
        agent=create_agent(
            model="claude-sonnet-5-5",
            tools= tool,
            system_prompt="you are a helpful task management assistant",
            checkpointer=InMemorySaver()
        )
        config={"configurable":{"thread_id":str(uuid4())}}
        human_question ="Can you Help me?"

        print("Agent Response:")
        while human_question!="q":
            result= await agent.ainvoke({"messages":[HumanMessage(content=human_question)]},config=config)

            print(result["messages"][-1].text)
            human_question=input("type message (q to exit):\n")


        #await agent.invoke({"message":[HumanMessage(content="Find the task titled 'Prepare MCP Demo Slides' in my database and change its status to 'in_progress'. " \
        #"Then retrieve the tasks again to verify the change. Do not create any new tasks.")]})
        
if __name__=="__main__":
    asyncio.run(main())