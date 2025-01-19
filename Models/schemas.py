"Schemas for the script"
from typing import Optional

from pydantic import BaseModel

class ContactInfo(BaseModel):
    """Data model for contact info"""
    email: Optional[str] = None
    phone: Optional[str] = None


class CustomerData(BaseModel):
    """Data model for customer data"""
    name: str
    contact_info: ContactInfo

class PaymentData(BaseModel):
    """Data model for payment data"""
    amount: int
    source: str
