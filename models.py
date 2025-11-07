from pydantic import BaseModel


class Product(BaseModel):
    id:int
    name:str
    quantity:int
    description:str
    price:float
    