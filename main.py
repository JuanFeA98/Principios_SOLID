"Entry point"
import os
from datetime import datetime, timedelta

import stripe
from dotenv import load_dotenv

from src.payment_processor import PaymentProcessor

_ = load_dotenv()
date = datetime.now() + timedelta(0)


def run():
    """___"""

    # Variables globales
    stripe.api_key = os.getenv("STRIPE_API_KEY")

    # Data
    customer_data_with_email = {
        "name": "John Doe",
        "contact_info": {"email": "e@mail.com"},
    }

    customer_data_with_phone = {
        "name": "Platzi Python",
        "contact_info": {"phone": "1234567890"},
    }

    payment_data = {
        "amount": 500, 
        "source": "tok_mastercard", 
        "cvv": 123
    }

    # Payment process wit email
    payment_processor = PaymentProcessor(customer_data_with_email, payment_data, date)

    payment_processor.process_transaction()
    payment_processor.notifier()

    # Payment process wit phone
    payment_processor = PaymentProcessor(customer_data_with_phone, payment_data, date)

    payment_processor.process_transaction()
    payment_processor.notifier()

if __name__ == "__main__":
    run()
