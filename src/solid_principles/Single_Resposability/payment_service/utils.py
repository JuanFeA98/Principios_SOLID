"Utility Script"
import logging
from datetime import datetime
from email.mime.text import MIMEText

def config_logging(dia: int, append=True):
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
        filename=f'./Log/log_{dia}.txt',
        level=logging.INFO,
        format=log_format,
        filemode=filemode,
        encoding='utf-8'
    )

    # Inicializamos el logging
    logger = logging.getLogger()

    return logger

def date_to_number(date: datetime):
    """Change the format of datetime

    Args:
        date (datetime): date to format

    Returns:
        int: date in numeric format
    """
    return int(str(date).replace('-', '')[:8])

def send_email(contact_mail: str):
    """Function to send emails

    Args:
        contact_mail (str): mail to send the message
    """
    msg = MIMEText("Thank you for your payment.")
    msg["Subject"] = "Payment Confirmation"
    msg["From"] = "no-reply@example.com"
    msg["To"] = contact_mail
