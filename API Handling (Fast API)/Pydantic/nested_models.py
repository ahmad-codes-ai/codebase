from pydantic import BaseModel


class Address(BaseModel):
    city : str
    state : str
    code : int


class User(BaseModel):
    name : str
    age : int
    gender : str
    address : Address  # Another model as filed this is nesting


ad1_details = {'city':'lahore','state':'Punjab','code':12345}
address1 = Address(**ad1_details)

u1_details = {'name':'Ahmad','age':16,'gender':'male','address':address1}
user1 = User(**u1_details)


print(user1)
print(user1.address.state) # Accessing from adress object


# Exporting as python dict / json

python_dict = user1.model_dump()
json_format = user1.model_dump_json()

print(type(python_dict))
print(type(json_format))