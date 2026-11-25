from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional, Annotated

class User(BaseModel):  # Need to inherit from BaseModel in order to work
    name : str      # This is type validation 
    age : int

    # Both fields name and age are required if only one given code will crash

    weight : float
    married : Annotated[bool,Field(default=None, title='Marriage status')]

    email : str

    allergies : Optional[List[str]] = Field(default=None, max_length = 5) # To enforce that only values can be str we used typing module List
    contacts : Dict[str,str]  # If normal dict was there k:v could be of any datatype

    normal_list : list   # This must be a list but can have any data type of values in it 


    @field_validator('email') # This get the value of email and run the function to validate it
    @classmethod # It is used so the function run before creation of the object as soon as tried

    def validate_email(cls,value,info):  # the field validator will pass email to value parameter

        # Pydantic call it like this email_validator(Patient, "ahmad@gmail.com")

        # With classmethod we can also access the class variables but the ones in order before email so if name and age are initialized before email in order we can only access them if another var like x is initialized after it we cant access it. In this scenerio the allergies contact and normal list is not accessible using this apprch bcz in memory when we are validating the email they dont even exist by this time to use this we use a third var like info which have those var

        allowed_url = ['mezan.com','hbl.com']

        domain = value.split('@')[-1]

        actual_name = info.data['name']  # info.data is a dict can also use .get()

        if domain not in allowed_url:
            raise ValueError('This email not allowed')
        return value


    @field_validator('age',mode='after')   # by default the mode is after too
    @classmethod

    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        raise ValueError('Age must be between 0 and 100')

    

        

def add_user(user : User):
    print(f"Name: {user.name}\nAge: {user.age}")
    print(user.allergies)
    print("User added in db")

    print(type(user.name), type(user.age))


# Can be now reused in many other functions


u1 = {'name':'Ahmad','age':'16','weight':55.6,'married':False,'normal_list':[1,3.2,True,'str'], 'contacts':{'email':'ahmad@gmail.com'}, 'email':'abc@hbl.com'}

user1 = User(**u1)  # For '16' it will auto convert it into int
add_user(user1)


