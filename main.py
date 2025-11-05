from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from models import Product


app=FastAPI()


products=[
    Product(id=1,name='laptop',quantity=5),
    Product(id=3,name='iphone',quantity=6),
    Product(id=5,name='earbuds',quantity=2)
]


@app.get('/products')
def get_all_product():
    
    return products

@app.get('/product/{id}')
def get_product(id:int):
    for product in products:
        if product.id==id:
            return products
    return {'product not found'}

@app.post('/product')
def add_product(product:Product):
    for p in products:
        if p.id==product.id:
            raise HTTPException(status_code=404,detail='id already exists')
    products.append(product)
    return product

@app.put('/product')
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return 'Product added successfully'
    return 'Product not found'   


@app.delete('/product')
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return 'product deleted'

    return 'product not found'