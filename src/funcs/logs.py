""" Arquivo para logs """
import logging
from datetime import date
import os


def log():
    """
    Define o arquivo do log da automação para o momento da execução
    """
    project_name = 't2c_nav'
    dta = date.today().strftime('%Y_%m_%d')
    logging.basicConfig(filename=os.path.join(os.getcwd(), 'logs', f"{project_name}_{dta}.log"),
                        level=logging.INFO,
                        format="%(asctime)s :: %(levelname)s :: %(lineno)d \ :: %(message)s")


def print_and_log(msg: str, warning: bool=False):
    print(msg)
    if warning is True:
        logging.warning(msg)
    else:
        logging.info(msg)
