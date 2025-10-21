from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORKING_DIR_DOCKER, TIMEOUT_DOCKER

def getDockerCommandLineCodeExecutor():
    docker=DockerCommandLineCodeExecutor(
        image='amancevice/pandas',
        work_dir=WORKING_DIR_DOCKER,
        timeout=TIMEOUT_DOCKER
    )
    return docker


async def start_docker_container(docker):
    print("Starting Docker container for code execution...")
    await docker.start()
    print("Docker container started.")

async def stop_docker_container(docker):
    print("Stopping Docker container for code execution...")
    await docker.stop()
    print("Docker container stopped.") 