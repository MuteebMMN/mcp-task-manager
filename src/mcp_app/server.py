from typing import Literal
from uuid import uuid4

from fastmcp import FastMCP
from mcp_app.database import(
    get_all_tasks,
    save_task,
    update_task_status_in_db
)

mcp=FastMCP("MCP server Muteeb")

@mcp.tool(name="create_task", description="this tool is create to create new tasks")
def create_task(title:str, priority:str="medium", description:str="")->dict:
    """
    this function creates new tasks in our database
    """
    task_id=str(uuid4())
    status="to do"

    task={"task_id":task_id, "title":title, "description":description, "status":status, "priority":priority}
    save_task(task)

    return task

@mcp.tool(name="list_task", description="this tool provide allthe list of task in our database")
def list_task()->list[dict]:
    """
    This function return all the tasks present in our database
    """
    return get_all_tasks()

@mcp.tool(name="update_task_status", description="This tool will update a specific task status based on its ID")
def update_task_status(task_id:str, status:Literal["todo", "in_progress", "done"]) -> dict:
    """
    this function will update the status of a specific task based on its ID
    """
   
    return update_task_status_in_db(task_id, status)



if __name__=="__main__":
    mcp.run(transport="http", port=8000)
    create_task(title="this is second task",description="this is a test")