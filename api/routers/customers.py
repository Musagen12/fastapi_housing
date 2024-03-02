from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..schemas import CustomerCreate, CustomerResponse
from .. import models
from ..database import get_db

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

## Create a route where a customer can view their details based on their id contained in a JWT token

@router.post("/create_customer", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = models.Customer(customer_name=customer.customer_name, customer_password=customer.customer_password, customer_email=customer.customer_email)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


@router.put("/full_update", response_model=CustomerResponse, status_code=status.HTTP_200_OK)
def full_update(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    old_customer_query = db.query(models.Customer).filter(models.Customer.customer_id == customer_id)

    old_customer_details = old_customer_query.first()
    if old_customer_details == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id: {customer_id} doesn't exist!!!")
    
    updated_query = old_customer_query.update(customer.model_dump(), synchronize_session=False)
    db.commit()

    return old_customer_query.first()


@router.patch("/partial_update", status_code=status.HTTP_200_OK)
def partial_update(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    old_customer_query = db.query(models.Customer).filter(models.Customer.customer_id == customer_id)
    
    pass


@router.delete("/delete", status_code=status.HTTP_404_NOT_FOUND)
def delete(customer_id: int, db: Session = Depends(get_db)):
    old_customer_query = db.query(models.Customer).filter(models.Customer.customer_id == customer_id)

    old_customer_details = old_customer_query.first()
    if old_customer_details == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id: {customer_id} doesn't exist!!!")
    old_customer_query.delete()
    db.commit()

    return {"data": "Succesfully delete customer!!!"}
