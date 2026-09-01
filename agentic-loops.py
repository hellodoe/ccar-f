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
        model="claude-4-5",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )
    if response.stop_reason == "end_turn":
        print(response.content[0].text if response.content else "")
        break

    # Append assistant's response to conversation history
    messages.append({"role": "assistant", "content": response.content})

    # Process tool calls
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            tool_name = block.name
            tool_input = block.input
            tool_use_id = block.id

            if tool_name == "calculator":
                expr = tool_input.get("expression", "")
                try:
                    result = str(eval(expr, {"__builtins__": None}, {}))
                except Exception as e:
                    result = f"Error evaluating expression: {e}"
            elif tool_name == "web_search":
                query = tool_input.get("query", "")
                result = f"Search results for query: '{query}'"
            else:
                result = f"Tool '{tool_name}' not recognized."

            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tool_use_id,
                "content": result,
            })

    if tool_results:
        messages.append({"role": "user", "content": tool_results})
