from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI
from tool_sets import summarize_website_tool, real_time_search_tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
import yaml
from utility import format_planner_output,transform_str_to_list
import random
from datetime import date


# configure .env file
env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

# initiate the model
llm = ChatOpenAI(model = "gpt-4o-mini")

# initiate tool sets
summarize_website_tool_instance = summarize_website_tool("https://www.google.com/")
real_time_search_tool_instance = real_time_search_tool("initiate")
available_tools = {
    "summarize_website": summarize_website_tool_instance,
    "real_time_search": real_time_search_tool_instance
}

# load config
with open("config/agent.yaml", "r") as f:
    agent_config = yaml.safe_load(f)

# initiate agents
agents = {}
for agent_name, config in agent_config.items():
    role = config.get("role")
    goal = config.get("goal")
    tool_names = config.get("tools")
    
    tools_for_agent = []
    if tool_names:
        for i in tool_names:
            tools_for_agent.append(available_tools[i])
    if role and goal:
        current_date = date.today().strftime("%Y-%m-%d")
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f" Tooday's date is {current_date}. You are a {role}, and you are responsible to {goal}.",
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        agent =  create_tool_calling_agent(llm, tools_for_agent, prompt)
        agent_executor = AgentExecutor(
            agent = agent, 
            tools = tools_for_agent, 
            memory=memory, 
            verbose = True
        )

        agents[agent_name] = agent_executor
        print(f"Initialized agent: {agent_name}")
    else:
        print(f"Warning: Skipping agent '{agent_name}' due to missing role or goal.")

# ------- work flow -------
def execute_workflow(quiry):
        attempt = 0
        max_attempt = 3
        retry_probability_threshold = 0.8

        while attempt < max_attempt:
            strategy_planner_agent = agents.get("strategy_planner")
            if strategy_planner_agent:
                try:
                    planner_output = strategy_planner_agent.invoke({"input": quiry})["output"]
                    planner_output_dic = format_planner_output(planner_output) 

                    # all results 
                    action_results = []
                    for agent_name in planner_output_dic:
                        for task in planner_output_dic[agent_name]:
                            result = agents[agent_name].invoke({"input": task})["output"]
                            action_results.append(result)


                    # use summarizer to incoorparate quiry and action_results, to get a final result
                    summarize_agent = agents.get("summarizer")
                    summarized_response = transform_str_to_list(summarize_agent.invoke({"input": f" Summary {action_results} in order to answer {quiry}"})["output"])
                    code = summarized_response[0]
                    message = summarized_response[1]

                    if code == 200:
                        # Generate a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive), potentially used to activate retry mechanism
                        random_probability = random.random()
                        if random_probability > retry_probability_threshold and attempt < max_attempt - 1:
                            quiry = f"{quiry}, with provided background which is {summarized_response[1]}, your result should be differnt than your last time"
                            attempt += 1
                            continue
                        else:
                            return {
                                "code": code,
                                "message": message
                            }

                    elif code == 400:
                        return {
                                "code": code,
                                "message": message
                            }
                except Exception as e:
                    return {
                            "code":500, 
                            "message": "Strategy planner agent not found."
                    }
                
        

                