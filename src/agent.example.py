import os
import requests
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.middleware import SummarizationMiddleware

from dotenv import load_dotenv


@tool("get_weather_info")
def get_weather_info(place: str, start:str, end:str) -> str:
    """Calling Free Weather API (https://open-meteo.com/en/docs) to get weather info.

    Args:
        place (str): The name of the place to get weather info for.
        start (str): The start date in ISO8601 date format.
        end (str): The end date in ISO8601 date format.
    """
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={place}&count=1&language=en&format=json"
    geo_response = requests.get(geocoding_url)
    geo_data = geo_response.json()

    if not geo_data.get("results"):
        return f"Could not find location information for '{place}'."

    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    name = location["name"]
    country = location.get("country", "")

    print(f"Now getting weather info for {lat}, {lon} ({name}, {country}) from {start} to {end}...")

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date={start}&end_date={end}&daily=weather_code,temperature_2m_max,temperature_2m_min"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    return weather_data


@tool("follow_up")
def follow_up(question: str) -> str:
    """Ask the user a follow-up question to gather more information."""
    return input(f"{question}: ")


def parse_response(result: dict) -> str:
    messages = result.get("messages", [])
    if not messages:
        return ""
    ans = messages[-1].content
    if "<|assistant|>" in ans:
        ans = ans.split("<|assistant|>")[1].strip()
    return ans


def main():
    load_dotenv()

    system_prompt = """You are a helpful assistant that answers questions that is related to weather. 
    Always consult the 'get_weather_info' tool to get relevant information.
    Answer the user's question to the best of your ability."""

    model = os.environ.get("CHAT_MODEL")
    if not model:
        print("Please set CHAT_MODEL environment variable.")
        exit()

    agent = create_agent(
        model=model,
        tools=[get_weather_info, follow_up],
        middleware=[
            SummarizationMiddleware(
                model=model,
                trigger=("tokens", 4000),
                keep=("messages", 20),
            ),
        ],
        system_prompt=system_prompt,
    )

    print("=== Welcome to the weather assistant! ===")
    question = input("Ask a question: ")

    print("Ok, let me see...")

    result = agent.invoke({"messages": [{"role": "user", "content": question}]})

    print(parse_response(result))

    print("============")


if __name__ == "__main__":
    main()
