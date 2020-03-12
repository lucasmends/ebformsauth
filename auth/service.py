import logging


logger = logging.getLogger(__name__)

APLICATION_URL = ' '



def get_user(identidade, senha):
    try:
        return {"identidade": "asdasd", "cpf": "000.000.000-00"}
    except:
        logger.error("Erro na interface de login")
        return None

    