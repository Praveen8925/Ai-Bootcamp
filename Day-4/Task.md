*Exercise 1 — Define three Tools*

Define two tools using the LangChain @tool decorator:
- web_search(query: str) — uses Tavily (TavilySearchResults) to fetch real-time web results for any topic.
- summarize(text: str) — sends the text to ChatOllama (model: llama3.2:3b) with a summary prompt and returns a short paragraph summary.
  - notes(text:str) - convert the latest response from the ai model to save in as notes with title and content. 

Test each tool standalone before connecting them to any agent.

⸻

*Exercise 2 — Build a Manual Tool-Calling Loop*

Build a manual agent loop where:
- The LLM receives a system prompt listing the available tools
- The LLM responds with a JSON tool call: {"tool": "tool_name", "args": {"param": "value"}}
- Your code parses the JSON, executes the matching tool, and feeds the result back to the LLM
- The loop continues until the LLM returns a final_answer

⸻

*Exercise 3 — Test with Three Queries*

Run your agent loop with the following queries and print which tool was picked at each step:
- "What is the latest news on OpenAI?" → should route to web_search
- "Summarize this paragraph: ..." (provide a paragraph) → should route to summarize
- "Find the latest news on AI agents and summarize it" → should call web_search first, then summarize (bonus)

⸻

*Exercise 4 (Bonus) — ReAct Agent with LangChain*

Recreate the same tool-calling behavior using create_react_agent from LangGraph with the same two tools. Run the same three queries and compare the output with your manual loop.

⸻

*Deliverable:* A single Python file day4_tool_calling.py containing both tool definitions, the manual agent loop, and example runs showing the tool the LLM picked for each query.

*Key takeaway:* Tools are just Python functions the LLM decides to invoke. Tool calling is the LLM outputting a structured JSON request — your code does the actual execution. This is the foundation of every AI agent.

