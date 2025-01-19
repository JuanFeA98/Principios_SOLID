"Function to configurate logging setting"
import logging

def run(dia: int, append=True):
    """Function to configurate logging setting

    Args:
        dia (int): log date 
        append (bool, optional): Option to overwrite or add information to the log. 
                                Defaults to True.
    """

    # Especificamos el formato del logging
    log_format = "%(levelname)s %(asctime)s - %(message)s"

    # Definimos el modo de escritura
    filemode = 'a' if append is True else 'w'

    # Configuramos nuestro logging
    logging.basicConfig(
        filename=f'./Log/log_{dia}.log',
        level=logging.INFO,
        format=log_format,
        filemode=filemode,
        encoding='utf-8'
    )

    # Inicializamos el logging
    logger = logging.getLogger()

    return logger
