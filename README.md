# mcp-task-manager

A small task manager exposed as an [MCP](https://modelcontextprotocol.io) server (FastMCP, SQLite), plus clients that talk to it, including a LangChain agent backed by Claude.

## Tools

| Tool | Purpose |
|------|---------|
| `create_task` | Create a task (`title`, optional `priority`, `description`) |
| `list_task` | List all tasks |
| `update_task_status` | Set a task's status (`todo`, `in_progress`, `done`) by ID |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
echo ANTHROPIC_API_KEY=your-key > .env   # only needed for the LangChain client
```

## Run

```sh
uv run python src/mcp_app/server.py          # MCP server on http://127.0.0.1:8000/mcp
uv run python src/mcp_app/langchain_client.py # chat agent using the server's tools
```

`.mcp.json` registers the server for Claude Code.

## Layout

- `src/mcp_app/server.py` – MCP server and tool definitions
- `src/mcp_app/database.py` – SQLite persistence
- `src/mcp_app/client.py`, `langchain_client.py` – clients
