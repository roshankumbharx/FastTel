from fastapi import FastAPI,HTTPException,Depends
from models import Product
import database_model
from databse import engine,session
from sqlalchemy.orm import Session

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)


products = [
    Product(id=1,name='laptop',quantity=5),
    Product(id=3,name='iphone',quantity=6),
    Product(id=5,name='earbuds',quantity=2)
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db=session()
    count = db.query(database_model.Product).count
    if count==0: 
        db = session()
        for product in products:
            db.add(database_model.Product(**product.model_dump()))
        db.commit()

init_db()

@app.get('/')
def get_products(db : Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()    
    return db_products

@app.get('/products/{id}')
def get_product_by_id(id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
    try:
        if db_product.id ==id:
            return db_product
    except:
        raise HTTPException(status_code=404,detail='id Not Found')
    

@app.post('/product')
def create_product(product:Product,db:Session = Depends(get_db)):
    try:
        db.add(database_model.Product(**product.model_dump()))
        db.commit()
        return product
    except:
        HTTPException(status_code=404,detail='pls fill in the details carefully')


@app.put('/product')
def update_product(id:int,product:Product,db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.quantity=product.quantity
        db.commit()
        return {'Product updated'}
    else:
        return 'Error Updating the product'
            

@app.delete('/product')
def delete_product(id:int,db:Session = Depends(get_db)):
    try:    
        db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
        if db_product:
            db.delete(db_product)
            db.commit()           
            return {'product deleted successfully'}
    except:
        HTTPException(status_code=404,detail='id not found')