# this file contains basic get,put,post and delete operations using fastapi

from fastapi import FastAPI,HTTPException


app=FastAPI()

@app.get('/')
def hello():
    return 'Running from port 8001'


items={}


@app.get('/items/{item_id}')
def get_item(item_id):
    if item_id in items:
        return item_id,items[item_id]
    else:
        return 'Item not found'
    
@app.post('/items/{item_id}')
def create_item(item_id,name):
    items[item_id]=name
    return {'message':f'item{item_id} created'}

@app.put('/items/{item_id}')
def update_item(item_id,name):
    if item_id in items:
        items[item_id]=name
        return {'message':'item updated'}
    else:
        raise HTTPException(status_code=404,detail='item not found')
    
@app.delete('/items/{item_id}')
def delete_item(item_id):
    if item_id in items:
        items.pop(item_id)
        return {'message':'Item deleted Succesfully'}
    else:
        raise HTTPException(status_code=404,detail='Item does not exist')