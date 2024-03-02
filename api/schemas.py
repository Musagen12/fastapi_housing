from pydantic import BaseModel
from datetime import datetime

########### Customer schemas ###########
class CustomerBase(BaseModel):
    customer_name: str 
    customer_email: str

class CustomerCreate(CustomerBase):
    customer_password: str
    
class CustomerResponse(CustomerBase):
    customer_id: int
    customer_password: str
    created_at: datetime

    class Config:
        from_attributes = True