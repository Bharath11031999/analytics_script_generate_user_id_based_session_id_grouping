import os
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(script_dir))
env_path = os.path.join(project_dir, 'cron_env', '.env')
load_dotenv(dotenv_path=env_path)


def get_env() -> str:
    """
    This is the method to fetch the env from the .env file
    :return: None by default & env_name if fetched from .env file
    """

    env = os.getenv('ENV')
    return env
