#!/usr/bin/env python3
"""Friday - A helpful command-line assistant powered by AI."""

import asyncio
from agentscope.agent import Agent
from agentscope.model import OpenAIChatModel
from agentscope.credential import OpenAICredential
from agentscope.message import UserMsg
from agentscope.event import TextBlockDeltaEvent, TextBlockStartEvent, TextBlockEndEvent
from config import settings
from logger_config import setup_logging

# 配置日志系统
logger = setup_logging()

# Streaming speed control (in seconds)
# Adjust this value to control output speed:
# 0.01 = fast, 0.03 = medium, 0.05 = slow
STREAM_DELAY = 0.03


async def main():
    logger.info("=" * 60)
    logger.info("Friday AI Assistant 启动中...")
    logger.info("=" * 60)
    
    # Get current model configuration
    logger.info(f"正在加载配置: MODEL_PROVIDER={settings.MODEL_PROVIDER}")
    model_config = settings.llm_config
    
    logger.info(f"模型配置加载成功:")
    logger.info(f"  - Base URL: {model_config['base_url']}")
    logger.info(f"  - Model Name: {model_config['model_name']}")
    logger.info(f"  - API Key: {model_config['api_key'][:10]}..." if model_config['api_key'] else "  - API Key: (未配置)")
    logger.info(f"  - Temperature: {settings.TEMPERATURE}")
    logger.info(f"  - Max Tokens: {settings.MAX_TOKENS}")
    
    logger.info("正在初始化 OpenAI 凭证...")
    credential = OpenAICredential(
        api_key=model_config["api_key"],
        base_url=model_config["base_url"]
    )
    logger.info("凭证初始化完成")

    logger.info("正在创建模型实例...")
    model = OpenAIChatModel(
        credential=credential,
        model=model_config["model_name"],
        parameters=OpenAIChatModel.Parameters(
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
        )
    )
    logger.info(f"模型实例创建成功: {model_config['model_name']}")

    logger.info("正在创建 Agent...")
    agent = Agent(
        name="Friday",
        system_prompt="You are a helpful assistant named Friday.",
        model=model,
    )
    logger.info("Agent 创建成功")

    print("=" * 60)
    print(f"Friday - Your AI Assistant (Using {settings.MODEL_PROVIDER.upper()})")
    print("=" * 60)
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    logger.info("进入对话循环...")
    conversation_count = 0

    while True:
        user_input = input("🍭 You: ").strip()

        if not user_input:
            logger.debug("用户输入为空，跳过")
            continue

        if user_input.lower() in ["exit", "quit"]:
            logger.info("用户请求退出")
            print("\n✨ Friday: Goodbye! Have a great day!")
            logger.info("程序正常退出")
            break

        conversation_count += 1
        logger.info(f"[对话 #{conversation_count}] 用户输入: {user_input}")
        
        logger.debug("创建用户消息对象...")
        msg = UserMsg(name="User", content=user_input)
        logger.debug(f"消息对象创建完成: {msg}")

        print("🚀 Friday: ", end="", flush=True)
        
        logger.info(f"[对话 #{conversation_count}] 开始请求 AI 响应...")
        response_text = ""
        event_count = 0

        # Use streaming response with controlled speed
        try:
            async for event in agent.reply_stream(msg):
                event_count += 1
                
                if isinstance(event, TextBlockStartEvent):
                    logger.debug(f"[对话 #{conversation_count}] 收到 TextBlockStartEvent (事件 #{event_count})")
                    continue
                elif isinstance(event, TextBlockDeltaEvent):
                    if hasattr(event, 'delta') and event.delta:
                        logger.debug(f"[对话 #{conversation_count}] 收到 TextBlockDeltaEvent (事件 #{event_count}): delta_length={len(event.delta)}")
                        response_text += event.delta
                        print(event.delta, end="", flush=True)
                        await asyncio.sleep(STREAM_DELAY)
                elif isinstance(event, TextBlockEndEvent):
                    logger.debug(f"[对话 #{conversation_count}] 收到 TextBlockEndEvent (事件 #{event_count})")
                    continue
                else:
                    logger.warning(f"[对话 #{conversation_count}] 收到未知事件类型: {type(event).__name__}")
            
            logger.info(f"[对话 #{conversation_count}] AI 响应完成:")
            logger.info(f"  - 总事件数: {event_count}")
            logger.info(f"  - 响应长度: {len(response_text)} 字符")
            logger.info(f"  - 响应内容: {response_text[:100]}..." if len(response_text) > 100 else f"  - 响应内容: {response_text}")
            
        except Exception as e:
            logger.error(f"[对话 #{conversation_count}] 处理响应时出错: {e}", exc_info=True)
            print(f"\n❌ 错误: {e}")

        print("\n")

if __name__ == "__main__":
    logger.info("程序启动...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("收到键盘中断信号 (Ctrl+C)")
        print("\n\n程序被用户中断")
    except Exception as e:
        logger.error(f"程序异常退出: {e}", exc_info=True)
        raise
    finally:
        logger.info("程序结束")
        logger.info("=" * 60)
