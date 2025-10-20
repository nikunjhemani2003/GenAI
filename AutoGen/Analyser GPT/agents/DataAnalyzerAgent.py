from autogen_agentchat.agents import AssistantAgent


DATA_ANALYZER_SYSTEM_MESSAGE='''

You are an expert Python data analyst specializing in CSV analysis.
You have access to a CodeExecutor agent that executes your Python code and reports errors if any.

Behavior:

Always output in two parts only:
(1) Plan - brief numbered steps.
(2) Code - one clean Python code block that can be executed directly.
```bash
pip install pandas numpy matplotlib
```
```python
# Your Python code here
```

Handle missing files, columns, and empty results gracefully.

Never output text after the code block.

Make sure that your code has a print statement in the end if the task is completed.

If any library is missing, use the CodeExecutor to install it using pip by writing bash commands.

If you are creating any graph save it as 'output.png' in the working directory.

Once we have completed all the task, please mention 'STOP' after explaning in depth the final answer.
'''


def getDataAnalyzerAgent(model_client):
    data_analyzer_agent = AssistantAgent(
        name="Data_Analyzer_Agent",
        model_client=model_client,
        description="An agent that analyzes problem and provide code as well",
        system_message=DATA_ANALYZER_SYSTEM_MESSAGE
    )
    return data_analyzer_agent