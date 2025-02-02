import asyncio
from langchain_anthropic import ChatAnthropic
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()


llm = ChatAnthropic(model="claude-3-sonnet-20240229")

async def main():
    agent = Agent(
        task="Compare the price of Claude-3 Sonnet and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
