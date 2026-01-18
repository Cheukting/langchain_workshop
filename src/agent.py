import os
from langchain.agents import create_agent
from langchain.tools import tool

from dotenv import load_dotenv


@tool("get_weather_info")
def get_weather_info(q: str) -> str:
    """Calling Free Weather API (https://open-meteo.com/en/docs) to get weather info."""
    # >>> chapter 2: create tool here
    pass


@tool("follow_up")
def follow_up(question: str) -> str:
    """Ask the user a follow-up question to gather more information."""
    # >>> chapter 2: create tool here
    pass


def parse_response(result: dict) -> str:
    # >>> chapter 2 (optional):parse response here
    return result


def main():
    load_dotenv()

    system_prompt = ""  # >>> chapter 1: add system prompt here

    model = os.environ.get("CHAT_MODEL")
    if not model:
        print("Please set CHAT_MODEL environment variable.")
        exit()

    agent = None  # >>> chapter 1: create an agent here

    print("=== Welcome to the weather assistant! ===")
    question = input("Ask a question: ")

    print("Ok, let me see...")

    result = agent.invoke({"messages": [{"role": "user", "content": question}]})

    print(parse_response(result))

    print("============")


if __name__ == "__main__":
    main()
