import asyncio
from teams.analyzer_gpt import getDataAnalyzerTeam
from config.docker_util import getDockerCommandLineCodeExecutor,start_docker_container,stop_docker_container
from models.gemini_model_client import get_model_client
from autogen_agentchat.messages import TextMessage



async def main():
    gemini_model_client = get_model_client()
    docker=getDockerCommandLineCodeExecutor()

    team= getDataAnalyzerTeam(docker,gemini_model_client)

    try:
        task="Can you give me a graph of types of flowers in my data iris.csv "

        await start_docker_container(docker=docker)
        async for message in team.run_stream(task=task):
            print(message)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        await stop_docker_container(docker=docker)
        await gemini_model_client.close()

if __name__ == "__main__":
    asyncio.run(main())