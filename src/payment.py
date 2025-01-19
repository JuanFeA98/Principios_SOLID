"Class to payments"
from datetime import datetime

import stripe

from Utils import config_logging, date_to_number

class Payment():
    """Class to payments"""

    def __init__(self, date: datetime):
        self.date = date
        self.logger = config_logging.run(date_to_number.run(self.date))

class StripePayment(Payment):
    """Class to payments in stripe"""
    def process_transaction(self, customer_data, payment_data):
        """Process to pay in stripe"""
        try:
            charge = stripe.Charge.create(
                amount=payment_data["amount"],
                currency="usd",
                source=payment_data["source"],
                description=f'Charge for {customer_data["name"]}',
            )

            self.logger.info("Transaction successful: %s", charge["id"])
            return charge

        except stripe.error.StripeError as e:
            self.logger.error("Stripe transaction failed: %s", str(e))
            raise RuntimeError("Transaction failed.") from e
