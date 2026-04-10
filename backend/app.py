import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://skyadmin:skypassword@db:5432/skybank_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Database Model
class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    balance = Column(Float)

app = FastAPI()

# 3. Pydantic Model for API requests
class TransferRequest(BaseModel):
    amount: float

@app.get("/api/v1/balance")
def get_balance():
    db = SessionLocal()
    # We fetch the account for 'Sky User' (id=1 from our init.sql)
    account = db.query(Account).filter(Account.id == 1).first()
    db.close()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"balance": float(account.balance), "currency": "USD"}

@app.post("/api/v1/transfer")
def transfer_funds(request: TransferRequest):
    db = SessionLocal()
    account = db.query(Account).filter(Account.id == 1).first()
    
    if account.balance < request.amount:
        db.close()
        return {"error": "Insufficient funds"}, 400
    
    # Update the balance in the database
    account.balance -= request.amount
    db.commit()
    db.refresh(account)
    db.close()
    
    return {"message": "Transfer successful", "new_balance": float(account.balance)}