from fastapi import FastAPI,Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,computed_field,Field
from typing import List,Optional,Annotated,Dict


app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(...,description="Id of the patient")]
    name : Annotated[str, Field(...,description="Name of the patient")]
    age : Annotated[int, Field(...,description="Age of patient",gt=0,le=120)]
    gender : Annotated[str, Field(...,description="Gender of the patient")]
    city: Annotated[str, Field(...,description="City of patient",max_length=50)]
    weight : Annotated[float,Field(...,gt=0,description="The weight of patient in kg")]
    height : Annotated[float,Field(...,gt=0,description="Height of patient in meters")]
    allergies : Optional[List[str]] = []
    contacts : Annotated[Dict[str,str],Field(...,description="Contact details of patient")]
    married : Annotated[bool,Field(...,description="Married status of patient")] 

    @computed_field
    @property

    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi



def load_patients():
    with open(r'C:\Users\Lenovo\Desktop\Projects\codebase\API Handling (Fast API)\Patients Record Backend\data.json','r') as f:
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
def show_patient(id:str = Path(..., description="Id of Patient", examples='P001')):
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


@app.post('/create')
def create_patient(patient : Patient):
    # patient is a object of Patient class means all data here if it pass comes validated as we need it if any error occur the fucntion will not be executed

    data = load_patients()

    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient already exist")

    data[patient.id] = patient.model_dump(exclude='id') # bcz id going as key

    with open(r'C:\Users\Lenovo\Desktop\Projects\codebase\API Handling (Fast API)\Patients Record Backend\data.json','w') as f:
        json.dump(data,f,indent=4)
        return JSONResponse(status_code=201,content={'message':'Patient added successfully'})
    

# app is a FastAPI class object 
# / is the base endpoint and then we have two more endpoints funny and play
# uvicorn is the web server which is reciving request and then running code 
# Only the first function inside a route will be executed no matter if it return anything or not
# The other functions are not linked to that route fastapi only know the immeditae next function under route
# ... in query or path means its required by client and has no default value set by server
