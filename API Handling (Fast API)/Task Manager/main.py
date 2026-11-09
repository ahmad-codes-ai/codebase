from fastapi import FastAPI, Body, HTTPException , status


tasks = {}


def add_task(name,des,status=False):
    task_id = len(tasks)+1

    tasks[task_id] = {'name':name,'description':des,'status':status}

    return task_id


def update_task(task_id,new_status=True):
    if task_id in tasks:
        tasks[task_id]['status'] = new_status
        return True
    return False


def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False 


def view_all_tasks():
    if len(tasks) > 0:
        return tasks
    return {}



app = FastAPI()


@app.get("/tasks")
def show():
    data = view_all_tasks()
    return data

@app.post("/addtask",status_code=status.HTTP_201_CREATED)
def add_to_tasks(data: dict = Body(...)):
    name = data.get('name')
    description = data.get('description')
    status = data.get('status',False)
    task_id = add_task(name,description,status)

    return {'task_id':task_id}


@app.put("/complete/{task_id}")
def complete_task(task_id: int):
    result = update_task(task_id)

    if not result:
       raise HTTPException(404,"Not Found")

    return {'task_id':task_id,'status':"completed"}


@app.delete("/delete/{task_id}")
def remove_task(task_id:int):
    result = delete_task(task_id)

    if not result:
        raise HTTPException(404,'Not Found')
    return {}





