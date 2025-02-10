"Class to notifications"
from datetime import datetime
from email.mime.text import MIMEText

from Utils import config_logging, date_to_number

class Notifier():
    """Class to notifications"""

    def __init__(self, date: datetime):
        self.date = date
        self.logger = config_logging.run(date_to_number.run(self.date))

class EmailNotifier(Notifier):
    """Notifications by email"""

    def send_notification(self, customer_data):
        """Send the comunication by email"""
        msg = MIMEText("Thank you for your payment.")
        msg["Subject"] = "Payment Confirmation"
        msg["From"] = "no-reply@example.com"
        msg["To"] = customer_data["contact_info"]["email"]


class SMSNotifier(Notifier):
    """Notifications by SMS"""

    def send_notification(self, customer_data):
        """Send the comunication by SMS"""
        phone = customer_data["contact_info"]["phone"]
        self.logger.info('SMS sent to %s: Thank you for your payment', phone)
