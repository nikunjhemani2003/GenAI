from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.DataAnalyzerAgent import getDataAnalyzerAgent
from agents.CodeExecutorAgent import getCodeExecutorAgent

def getDataAnalyzerTeam(docker,model_client):
    code_executor_agent = getCodeExecutorAgent(docker)
    data_analyzer_agent = getDataAnalyzerAgent(model_client=model_client)
    termination = TextMentionTermination("STOP")

    data_analyzer_team = RoundRobinGroupChat(
        name="Data_Analyzer_Team",
        participants=[
            data_analyzer_agent,
            code_executor_agent
        ],
        max_turns=10,
        termination_condition=termination
    )
    return data_analyzer_team