# 🚀 X17
## A Smart Agent, which can help you with daily inquiries


- Type some words in the text box
- Wait...boom
- ✨Magic ✨

<img src="/assets/entry.png" width="900">

## ⭐ Features 

- Answering User Queries
- Strategic Planning
- Real-time Information Retrieval
- Website Content Summarizations
- Integration with Language Models


An artificial intelligence (AI) agent refers to a system or program that is capable of autonomously performing tasks on behalf of a user or another system.
As mentioned on [Wikipedia](https://en.wikipedia.org/wiki/Intelligent_agent). 
> "
> Above, a canvas dark, with diamond light,
> The ancient stars ignite the endless night.
> Below, vast continents in slumber lie,
> Beneath the gaze of that celestial eye.
> From mountain peaks that pierce the starry dome,
> To shores where ocean whispers find their home,
> The cosmos vast, the solid earth so grand,
> A timeless wonder held within our hand
> "
> by AI

This text you see here is actually- written by AI! It is such a powerful tool!

## 👀 Tech

- Python 12.0 - A versatile and widely-used programming language.
- Langchain - A framework for developing applications powered by language models.
- Streamlit - A library for creating interactive web applications from Python scripts.

## 🔗 Structure

```
.
├── workflow.py            # Work flow
├── app.py                 # Streamlit frontend
├── config/                
│   └── agent.yaml         # Agent definitions
├── tool_sets.py           # Tools
├── utility.py             # Utilities
├── requiremenrs.txt       # Dependencies
├── .env                   # Environment variables
└── README.md
```

## 🧁 Installation
## 1. Clone the project
```
git clone https://github.com/RWXN/agent.git
cd Agent
pip install -r requirements.txt
```

## 2. Set up environment variable
```
TAVILY_API_KEY = YOUR_TAVILY_API_KEY
OPENAI_API_KEY = YOUR_OPENAI_API_KEY
```

## 3. Launch the App
```
streamlit run app.py
```

## ⚙️ How does it work
🔵 Agents ( config/agent.yaml )
Each AI agent has a role, capabilities(tools) and responsibily

|ROLE | Responsibily | CAPABILITY|
| ------ | ------ | ------ |
| Senior strategy planner | Divide inquiry into smaller tasks and make assignment |Summarize_Website, Real_Rime_Search|
| Senior web tasker| Navigate websites, extract info, summarize pages, process web resources|Summarize_Websit
| Senior real-time info tasker| Search internet for current info, answer about events, locate online data |Real_Rime_Search
| Senior information summarizer |Examine/summarize info, then answer user goal  |Default|


🔵 Tools ( tool_sets.py) 
Each customised tool provides particular capability to the agent

| TOOLS | README |
| ------ | ------ |
| real_time_search_tool | Useful for when you need to answer questions about current events. Input should be a search query|
| summarize_website_tool | Useful for summarizing content from a given website |


🔵 Work Flow ( workflow.py )
It sets up a system where different AI agents collaborate to answer user inquries. It starts by loading configurations and initializing the necessary tools and language model. Then, it creates several specialized agents, each with a specific role and the ability to use certain tools. When a user inputs a quiry, a "strategy planner" agent decides which agents and tools are needed. These agents then perform their tasks, and a "summarizer" agent compiles the results into a final answer for the user. The system also has a mechanism to retry the process.

## 🚥 Sample Interactions
Inquiry 1:
<img src="/assets/Inquiry_1_process.png" width="1200">


Inquiry 2:
<img src="/assets/Inquiry_2_process.png" width="1200">


Inquiry 3:
<img src="/assets/Inquiry_3_process.png" width="1200">


## 🚌 Future Improvement
- Let llm produce better quality prompt based on my original prompt
- Add multimodal to the system
- Change retry mechanism to actual industry criteria
- Use cache to save more recourses
