from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float

Base  = declarative_base()

class Product(Base):
    
    __tablename__  = 'anotherProduct'
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    quantity = Column(String)
    description = Column(String)
    price = Column(Float)
    