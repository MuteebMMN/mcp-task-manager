import asyncio
from fastmcp import Client


client=Client("http://127.0.0.1:8000/mcp")

async def get_tools_from_server():
    async with client:
        tools=await client.list_tools()

        for tool in tools:
            print(tool.name)

        return tools

async def create_task_using_mcp():
    async with client:
        result=await client.call_tool(
            "create_task",
            {
                "title":"task2",
                "priority": "high",
                "description":"this is a test from our client"
            }
        )

        print(result.data)
    return result.data

async def update_task_status_from_mcp():
    async with client:
        result= await client.call_tool(
            "update_task_status",
            {
                "task_id":"2163cec3-97cc-42d3-8133-18a9169b17bf",
                "status": "in_progress"
            }
        )
        print(result.data)
    return(result.data)   

async def list_tasks_using_mcp():
    async with client:
        result = await client.call_tool(
            "list_task"
        )

        print("these are all the tasks:")
        print(result.data)

    return result.data

if __name__=="__main__":
    asyncio.run(list_tasks_using_mcp())
    