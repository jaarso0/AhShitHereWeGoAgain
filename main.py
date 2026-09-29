from typing import List

from pydantic import BaseModel, Field 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from langchain_tavily import TavilySearch
load_dotenv()

# tavily = TavilyClient()

# class Source(BaseModel):


def main():
    print("Hello from langu!")
    result  = agent.invoke({"messages": [ HumanMessage(content="search for 3 job postings for an ai engineer using langchain in hyderabad and list their details")]})
    print(result)


class Source(BaseModel):
    """schema for source used by the agent"""

    url:str = Field( description="The url of the source")

class AgentResponse(BaseModel):
    """schema for the agent reply"""

    answer:str = Field( description="agent answer to the user query")
    sources:List[Source] = Field(default_factory =list, description="The sources used by the agent to generate the reply")



# @tool
# def TavilySearch(query: str) -> str:
#     """
#     Tool that searches over the internet
#     Args:
#         query : The query is to search for
#     Returns: 
#         The search result
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools = [TavilySearch(max_results=3, include_domains=["linkedin.com"])]
agent = create_agent(model=llm, tools=tools, response_format = AgentResponse)




if __name__ == "__main__":
    main()
