"Function to send emails"
from email.mime.text import MIMEText

def run(contact_mail: str):
    """Function to send emails

    Args:
        contact_mail (str): mail to send the message
    """
    msg = MIMEText("Thank you for your payment.")
    msg["Subject"] = "Payment Confirmation"
    msg["From"] = "no-reply@example.com"
    msg["To"] = contact_mail
