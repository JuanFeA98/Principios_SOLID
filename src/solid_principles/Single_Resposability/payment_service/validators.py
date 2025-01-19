"Classes to validate data"
from dataclasses import dataclass
from datetime import datetime

from utils import config_logging

@dataclass
class CustomerDataValidator():
    """Class to validate customer data"""
    def __init__(self, date: datetime):
        self.date = date
        self.day = int(str(self.date).replace('-', '')[:8])
        self.logger = config_logging(self.day, append=True)

    def validate(self, customer_data_info: dict):
        """Customer data valitation

        Args:
            customer_data (dict): dictionary with customer data

        Raises:
            ValueError: In case the customer data doesn't have name
            ValueError: In case the customer data doesn't have contact info
        """
        if not customer_data_info.get("name"):
            validation = False
            self.logger.info('Invalid customer data: missing name')
            # raise ValueError("Invalid customer data: missing name")

        if not customer_data_info.get("contact_info"):
            validation = False
            self.logger.info('Invalid customer data: missing contact info')
            # raise ValueError("Invalid customer data: missing contact info")

        else:
            validation = True

        self.logger.info('Customer data validated')

        return validation

@dataclass
class PaymentDataValidator():
    """Class to validate payment data"""
    def __init__(self, date: datetime):
        self.date = date
        self.day = int(str(self.date).replace('-', '')[:8])
        self.logger = config_logging(self.day, append=True)

    def validate(self, payment_data_info: dict):
        """_summary_

        Args:
            payment_data (dict): dictionary with payment data 

        Raises:
            ValueError: In case the payment data doesn't have source info
        """
        if not payment_data_info.get("source"):
            validation = False
            self.logger.info('Invalid payment data')
            # raise ValueError("Invalid payment data")

        else:
            validation = True

        self.logger.info('Payment data validated')
        return validation
