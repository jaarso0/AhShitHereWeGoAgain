agents: 
An agent is a software system that uses LLMs as a reasoning engine to decide what actions to take and then execute those actions.

chain: developer defined flow
agent: llm defined control flow

what is a ReAct agent:
its a specific type of agent architecture that follows the react paradigm

say

                    -----(observation)----|
                    |                     |
                    |    |-> Tool(action)-|
query -> llm(thinking) --|
                         |-> Answer 


what are tools: the ability we are giving the LLM that can be making an API call, calling db, running py code etc

Langchain and LangGraph gives us pre-built react agents

