import httpx


client = httpx.Client(
    base_url="http://127.0.0.1:8002"
)


def add_task(name,description,status=False):
    payload = {
        'name': name,
        'description': description,
        'status':status
    }
    result = client.post('/addtask',json=payload)

    if result.status_code == 201:
        return result.json()
    return False 


def complete_task(task_id):
    result = client.put(f'/complete/{task_id}')

    if result.status_code == 200:
        return True
    return False


def delete_task(task_id):
    result = client.delete(f'/delete/{task_id}')

    if result.status_code == 200:
        return True
    return False 

def view_all_tasks():
    result = client.get('/tasks')

    return result.json()




# Testing

t1 = add_task('Task 1 ',"This is task 1 ")
t2 = add_task('Tasks 2','This is task 2')

complete_task(t1['task_id'])


t = view_all_tasks()
print(t)

print()


delete_task(t1['task_id'])
print(view_all_tasks())