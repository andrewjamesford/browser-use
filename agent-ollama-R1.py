import asyncio
from langchain_ollama import ChatOllama
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()


llm = ChatOllama(model="deepseek-r1:14b", num_ctx=32000)

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
