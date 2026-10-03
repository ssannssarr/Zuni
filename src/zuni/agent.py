"""The tool-calling loop: ask, run requested tools, repeat, answer."""
from __future__ import annotations

from typing import Any, Callable

from zuni.errors import APIError, ZuniError
from zuni.llm.llm import LLM
from zuni.tools.schema import TOOLS
from zuni.tools.toolbox import Toolbox


class ToolsNotSupported(ZuniError):
    """The very first request failed, so this model/provider likely has no
    tool calling. The caller can fall back to plain search + answer."""


async def run_agent(
    llm: LLM,
    chat: list[dict[str, Any]],
    toolbox: Toolbox,
    max_steps: int = 4,
    on_tool: Callable[[str, dict[str, Any]], None] | None = None,
) -> str:
    """Let the model call tools until it answers, then return the answer.

    ``chat`` is extended in place with the assistant and tool messages.
    After ``max_steps`` rounds of tool calls the model is asked, without
    tools, to answer with what it has.

    Raises:
        ToolsNotSupported: The first request was rejected by the API.
        ZuniError: Any other failure from the LLM layer.
    """
    for step in range(max_steps):
        try:
            res = await llm.ask(chat=chat, tools=TOOLS)
        except APIError as exc:
            if step == 0:
                raise ToolsNotSupported(str(exc)) from exc
            raise

        message = LLM.message(res)
        calls = message.get("tool_calls") or []
        if not calls:
            return LLM.text(res)

        chat.append({
            "role": "assistant",
            "content": message.get("content") or "",
            "tool_calls": calls,
        })
        for call in calls:
            function = call.get("function") or {}
            name = str(function.get("name", ""))
            try:
                args = Toolbox.parse_arguments(function.get("arguments"))
            except ValueError:
                result = "Error: tool arguments were not valid JSON."
            else:
                if on_tool is not None:
                    on_tool(name, args)
                result = await toolbox.run(name, args)
            chat.append({
                "role": "tool",
                "tool_call_id": str(call.get("id", "")),
                "content": result,
            })

    # Step budget used up: force a final answer without tools.
    chat.append({
        "role": "user",
        "content": "Answer now using only the information gathered so far.",
    })
    return LLM.text(await llm.ask(chat=chat))
