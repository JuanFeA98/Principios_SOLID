"Class for processing payment"
from datetime import datetime

import stripe

from src.validators import CustomerDataValidator, PaymentDataValidator
from Utils import config_logging, date_to_number, send_email

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
        try:
            charge = stripe.Charge.create(
                amount=self.payment_data["amount"],
                currency="usd",
                source=self.payment_data["source"],
                description=f'Charge for {self.customer_data["name"]}',
            )

            self.logger.info("Transaction successful: %s", charge["id"])
            return charge

        except stripe.error.StripeError as e:
            self.logger.error("Stripe transaction failed: %s", str(e))
            raise RuntimeError("Transaction failed.") from e

    def notifier(self):
        """Process to notificate the transaction"""

        if "email" in self.customer_data["contact_info"]:

            email = self.customer_data["contact_info"]["email"]
            send_email.run(email)
            self.logger.info('Email sent to %s', email)

        elif "phone" in self.customer_data["contact_info"]:

            phone = self.customer_data["contact_info"]["phone"]
            self.logger.info('SMS sent to %d: Thank you for your payment', phone)
