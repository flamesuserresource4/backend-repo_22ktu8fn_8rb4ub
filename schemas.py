"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# SaaS landing page contact / inquiry schema
class ContactMessage(BaseModel):
    """
    Contact messages from the landing page
    Collection name: "contactmessage"
    """
    name: str = Field(..., min_length=2, max_length=100, description="Sender full name")
    email: EmailStr = Field(..., description="Contact email")
    company: Optional[str] = Field(None, max_length=120, description="Company name")
    service: Optional[Literal['Website', 'SaaS Build', 'Design', 'Consulting', 'Other']] = Field(None, description="Requested service category")
    budget: Optional[Literal['< $5k', '$5k-$15k', '$15k-$50k', '$50k+']] = Field(None, description="Budget range")
    message: str = Field(..., min_length=10, max_length=2000, description="Project details or message")
