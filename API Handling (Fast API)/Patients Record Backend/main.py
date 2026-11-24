from fastapi import FastAPI,Path, HTTPException, Query
import json

app = FastAPI()

def load_patients():
    with open('data.json','r') as f:
        data = json.load(f)
    return data    


def sort_data(val,rev=False):
    patients = load_patients()

    sorted_patients = dict(
        sorted(patients.items(),
               key=lambda x: x[1][val],
               reverse=rev
        )
    )
    
    return sorted_patients


@app.get('/')
def home():
    return {'message':"Hello this is a patient management system"}

@app.get('/view')
def show_patients():

    data = load_patients()
    return data


@app.get('/view/{id}')
def show_patient(id:str = Path(..., description="Id of Patient", example='P001')):
    patients = load_patients()
    if id in patients:
        return patients[id]
    raise HTTPException(status_code=404,detail="Not Found")
    


@app.get('/sort')
def sort(sort_by: str = Query(..., description="Sort on the basis of height/weight/bmi"), order: str = Query('asc',description="The order in which to sort asc or desc")):
    valid_fields = ['height','weight','bmi']

    if sort_by not in  valid_fields:
        raise HTTPException(status_code=400,detail="Bad Request plz send correct field to sort")

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Bad Request plz send either asc/desc")
    
    rev = True if order == 'desc' else False
    data = sort_data(sort_by,rev)
    return data

    

# app is a FastAPI class object 
# / is the base endpoint and then we have two more endpoints funny and play
# uvicorn is the web server which is reciving request and then running code 
# Only the first function inside a route will be executed no matter if it return anything or not
# The other functions are not linked to that route fastapi only know the immeditae next function under route
# ... in query or path means its required by client and has no default value set by server
