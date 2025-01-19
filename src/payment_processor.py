"Class for processing payment"
from datetime import datetime

from src.validators import CustomerDataValidator, PaymentDataValidator
from src.payment import StripePayment
from src.notifier import EmailNotifier, SMSNotifier

from Utils import config_logging, date_to_number

class PaymentProcessor:
    """Class for processing payments."""

    def __init__(self, customer_data: dict, payment_data: dict, date: datetime):
        self.customer_data = customer_data
        self.payment_data = payment_data
        self.date = date
        self.is_customer_data_valid = False
        self.is_payment_data_valid = False
        self.logger = config_logging.run(date_to_number.run(self.date), append=True)

    def customer_data_validation(self):
        """Validation of customer data"""

        customer_validator = CustomerDataValidator(self.date)
        self.is_customer_data_valid = customer_validator.validate(self.customer_data)

    def payment_data_validation(self):
        """Validation of payment data"""

        payment_validator = PaymentDataValidator(self.date)
        self.is_payment_data_valid = payment_validator.validate(self.payment_data)

    def process_transaction(self):
        """Process payment transaction using Stripe."""
        self.logger.info("-------------------------------")
        self.logger.info("Starting payment procces.")

        # Validation of the data
        self.customer_data_validation()
        self.payment_data_validation()

        # Payment process
        stripe_payment = StripePayment(self.date)
        stripe_payment.process_transaction(self.customer_data, self.payment_data)

    def notifier(self):
        """Process to notificate the transaction"""

        if "email" in self.customer_data["contact_info"]:

            email_notifier = EmailNotifier(self.date)
            email_notifier.send_notification(self.customer_data)

            self.logger.info('Email sent')

        elif "phone" in self.customer_data["contact_info"]:

            sms_notifier = SMSNotifier(self.date)
            sms_notifier.send_notification(self.customer_data)

            self.logger.info('SMS sent')
