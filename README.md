In this workshop, we will build a simple AI agent using LangChain. We will look at some basic component when building an AI agent. Including LLM, tools and middleware.

## Prerequisites

- Hugging Face Hub account or any account with [other AI providers](https://docs.langchain.com/oss/python/integrations/providers/overview)
- Intermidiate Python experiance
- Basic understanding of AI and natural language processing concepts

## Introduction to LangChain

LangChain is a Python library for building AI agents. It provides a simple and consistent interface for connecting to a variety of LLMs and other AI tools.

In this workshop, we will start with a skeleton of an AI agent in the /src folder. This is just a basic template that is easy to start with, you can add more functionality to it later.

In each chapter, there will be step by step instruction to build the example agent. However, you are encourage to write your own code to improve it or modify its funtionality once you are familiar with it.

## Chapter 1 - Connecting to an LLM

The benifit of using LangChain is that it abstracts away the complexity of connecting to a large variaty of LLM provided by many popular providers. Including OpenAI, Antropic and Hugging Face.

If you already have an account to any provider support, feel free to us it. However, be aware that most of the provider will charge you for using their API service. Check the price list before you decide to use them.

If you do not want to use any paid provider, you can use Hugging Face Hub as your AI provider. This way you will be using an open source LLM locally. This may mean you will have to have PyTorch or Tensorflow installed locally on top of other requirements.

First, use the [`create_agent`](https://reference.langchain.com/python/langchain/agents/?_gl=1*baxhnz*_gcl_au*Mzg1NzM1NDUxLjE3NjUyMDk4OTg.*_ga*MTk1ODUyNzE1Ny4xNzY1MjA5ODk4*_ga_47WX3HKKY2*czE3Njg2OTU0MjAkbzIwJGcxJHQxNzY4Njk1NDQ4JGozMiRsMCRoMA..#langchain.agents.create_agent) provided by LangChain to create an agent.

To start create a model, provide a model, a tool and a system prompt.

- model: It cen be infered by LangChain (example "gpt-5") or you can provide the model provider name in the format of "openai:gpt-5") See [here](https://reference.langchain.com/python/langchain/models/?_gl=1*12ht130*_gcl_au*Mzg1NzM1NDUxLjE3NjUyMDk4OTg.*_ga*MTk1ODUyNzE1Ny4xNzY1MjA5ODk4*_ga_47WX3HKKY2*czE3Njg2OTU0MjAkbzIwJGcxJHQxNzY4Njk1ODAyJGoyNCRsMCRoMA..#langchain.chat_models.init_chat_model(model))
- tool: Tools can be created with the `@tool` decorator, in this example we will create two tools `get_weather_info` and `follow_up` in the next chapter.
- system prompt: This is the instruction to provide the agent a role, and procide clear instruction what is expected behavior from the agent. For example, in our case, we will tell the agent to provide weather information for a specific location. It will also consult the `get_weather_info`.

Now follow the comment in the `agent.py` to fill in the blanks for this chapter.

## Chapter 2 - Adding tools to your agent

One of the major different of an AI agent to a simple chatbot is that it can be extended with tools. And these tools can help the agent to complete the specific task that the use required.

In this chapter, we will add some tool(s) to your agent. It is up to you to decide what tools to give your agent. Usually these tools are used to complete a specific task. For example, I would like the agent to be able to ge the latest weather forecast for a specific location. Therefore, I will add a weather searching tool to my agent. Another useful tool to have, is to provide a way to get follow up information from the user.

Creating tools with LangChain is very simple, just add the `@tool` decorator to the function and LangChain can take it as a tool in the agent.

Follow the comment in the `agent.py` to fill in the blanks for the tools.

Now you can test the agent. Optionally, you may want to extract the meaning message of the output from the resulting dictionary and only print the message. You can do it with `parse_result`.

## Chapter 3 - Adding middleware

Another benifit of using LangChain is that it provides a simple way to add middleware to your agent. Middleware is a piece of code that can be used to intercept and modify the input and output of your agent. See [here](https://docs.langchain.com/oss/python/langchain/middleware/built-in) for a list of available middleware. You can also create your own middleware, see [here](https://docs.langchain.com/oss/python/langchain/middleware/custom) about how to create a custom middleware.

In our example, we will simply add the [SummarizationMiddleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in#summarization) in case the message sending to the model is too long. This will be very useful if there's a lot of back-and-forth conversation betweent eh agent and the user.

Follow [the example](https://docs.langchain.com/oss/python/langchain/middleware/built-in#summarization) in the documentation to add the middleware to your agent.

After you finish the chapter, you may add extra functionality to your agent, like extra tools or middleware. You can also try creating your own agent and perform a complete different task.

---

## Support this workshop

This workshop is created by Cheuk and is open source for everyone to use (under MIT license). Please consider sponsoring Cheuk's work via [GitHub Sponsor](https://github.com/sponsors/Cheukting).


