#!/usr/bin/env python3
"""Friday - A helpful command-line assistant powered by AI."""

import asyncio
from agentscope.agent import Agent
from agentscope.model import OpenAIChatModel
from agentscope.credential import OpenAICredential
from agentscope.message import UserMsg
from agentscope.event import TextBlockDeltaEvent, TextBlockStartEvent, TextBlockEndEvent
from config import settings

# Streaming speed control (in seconds)
# Adjust this value to control output speed:
# 0.01 = fast, 0.03 = medium, 0.05 = slow
STREAM_DELAY = 0.03


async def main():
    # Get current model configuration
    model_config = settings.llm_config
    
    credential = OpenAICredential(
        api_key=model_config["api_key"],
        base_url=model_config["base_url"]
    )

    model = OpenAIChatModel(
        credential=credential,
        model=model_config["model_name"],
        parameters=OpenAIChatModel.Parameters(
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
        )
    )

    agent = Agent(
        name="Friday",
        system_prompt="You are a helpful assistant named Friday.",
        model=model,
    )

    print("=" * 60)
    print(f"Friday - Your AI Assistant (Using {settings.MODEL_PROVIDER.upper()})")
    print("=" * 60)
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("🍭 You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("\n✨ Friday: Goodbye! Have a great day!")
            break

        msg = UserMsg(name="User", content=user_input)

        print("🚀 Friday: ", end="", flush=True)

        # Use streaming response with controlled speed
        async for event in agent.reply_stream(msg):
            if isinstance(event, TextBlockStartEvent):
                # Start of a text block
                continue
            elif isinstance(event, TextBlockDeltaEvent):
                # Stream the text delta with a slight delay for readability
                if hasattr(event, 'delta') and event.delta:
                    print(event.delta, end="", flush=True)
                    # Add small delay to make streaming more readable
                    await asyncio.sleep(STREAM_DELAY)
            elif isinstance(event, TextBlockEndEvent):
                # End of a text block
                continue

        print("\n")


if __name__ == "__main__":
    asyncio.run(main())
