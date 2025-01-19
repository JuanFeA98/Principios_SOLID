"Classes to validate data"
from datetime import datetime

from Utils import config_logging

class CustomerDataValidator():
    """Class to validate customer data"""
    def __init__(self, date: datetime):
        self.date = date
        self.day = int(str(self.date).replace('-', '')[:8])
        self.logger = config_logging.run(self.day, append=True)

    def validate(self, customer_data_info: dict):
        """Customer data valitation

        Args:
            customer_data (dict): dictionary with customer data
        """
        if not customer_data_info.get("name"):
            validation = False
            self.logger.info('Invalid customer data: missing name')

        if not customer_data_info.get("contact_info"):
            validation = False
            self.logger.info('Invalid customer data: missing contact info')

        else:
            validation = True

        self.logger.info('Customer data validated')

        return validation

class PaymentDataValidator():
    """Class to validate payment data"""
    def __init__(self, date: datetime):
        self.date = date
        self.day = int(str(self.date).replace('-', '')[:8])
        self.logger = config_logging.run(self.day, append=True)

    def validate(self, payment_data_info: dict):
        """Payment data validation

        Args:
            payment_data (dict): dictionary with payment data 
        """
        if not payment_data_info.get("source"):
            validation = False
            self.logger.info('Invalid payment data')

        else:
            validation = True

        self.logger.info('Payment data validated')
        return validation
