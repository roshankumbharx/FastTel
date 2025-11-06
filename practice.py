from fastapi import FastAPI,HTTPException
from models import Product
import database_model
from databse import engine,session

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)


products = [
    Product(id=1,name='laptop',quantity=5),
    Product(id=3,name='iphone',quantity=6),
    Product(id=5,name='earbuds',quantity=2)
]


def init_db():
    db = session()
    for product in products:
        db.add(database_model.Product(**product.model_dump()))
    db.commit()

init_db()

@app.get('/')
def get_products():    
    return products

@app.get('/products/{id}')
def get_product_by_id(id:int):
    for product in products:
        if product.id ==id:
            return product
    raise HTTPException(status_code=404,detail='Not Found')
    

@app.post('/product')
def create_product(product:Product):
    products.append(product)
    return products


@app.put('/product')
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i] = product
            return products
    
    return 'Error Updating the product'
            

@app.delete('/product')
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            products.pop(i)
            return products
    return 'Error deleting the product' 