import ast

# ------- Extracts tasks and tools from planner output ------- 
def format_planner_output(planner_output_str):
    tasks_by_tool = {}
    try:
        for line in planner_output_str.split('\n'):
            parts = None
            if "Tool selected for this task:" in line or "tool selected for this task:" in line:
                parts = line.split("Tool selected for this task:")
            if "tool selected for this task:" in line:
                parts = line.split("tool selected for this task:")
            task_part = parts[0].replace("task need to be done:", "").strip()
            tool_part = parts[1]
            if "." in parts[1]:
                tool_part = parts[1].strip().replace('.', '')
            if "," in parts[1]:
                tool_part = parts[1].strip().replace(',', '')
            tool_name = tool_part.strip()
            task_description = task_part.strip()

            if tool_name not in tasks_by_tool:
                tasks_by_tool[tool_name] = []
            tasks_by_tool[tool_name].append(task_description)
    except Exception as e:
        print(f"Error formatting planner output {planner_output_str}: {e}")

    return tasks_by_tool

# ------- Transform a list alike string to a list -------
def transform_str_to_list(str):
    python_list = ast.literal_eval(str)
    return python_list



