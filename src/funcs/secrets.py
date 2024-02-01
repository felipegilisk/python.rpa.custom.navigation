import os
from dotenv import load_dotenv


def load_settings():
    """
    Carrega o conteúdo do arquivo .env ou .env.hml como variáveis de ambiente
    """
    env = os.getenv('ENVIRONMENT')
    env_file = f'.env{"." + env.lower() if env else ""}'
    load_dotenv(dotenv_path=env_file)
