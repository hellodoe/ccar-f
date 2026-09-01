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

