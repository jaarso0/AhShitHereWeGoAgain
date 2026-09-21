itnoatmmatmb

hello

Langchain: It is a framework that is used to make your LLMs as a blackbox and build around it, connect it to applicaitons, information/data through external websites or normal retrieval.

pretty popular these days



- PROMPT TEMPLATES: the first abstraction that langchain is introducing us is prompt templates. It help to translate the user input and params into instructions for llm. 
to guide the models response and help it understand context and generate relevant output.

chat model : class that is the primary interface we talk to llms, 
llms are converstational so they are effective when we provide them with the dialogue history - and that is the core of the chat model interface.
so we provide structured input  


A langchain chain is a work flow that connects multiple components in langchain together in sequence - where output of one step because input of another.


Langchain Expression Language (LCEL): in this lcel syntax we create a chain by composing two components
'|' Pipe Operator in an expression language is going to create a new runnable chain by connecting the output of the left component as an input to the right