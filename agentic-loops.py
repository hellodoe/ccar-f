# pyrefly: ignore [missing-import]
import anthropic
from dotenv import load_dotenv

load_dotenv()


client = anthropic.Anthropic()

tools = [
    {
        "name": "calculator",
        "description": "Evaluates a mathematical expression.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string"
                }
            },
            "required": ["expression"],
        },
    },
        {
        "name": "web_search",
        "description": "Performs a Google search.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string"
                }
            },
            "required": ["query"],
        },
    }
]


user_prompt = "Hello, world!"
messages = [{"role": "user", "content": user_prompt}]

while True:
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools,
        messages=messages
    )
    if response.stop_reason == "end_turn":
        break
    # Handle tool_use next

