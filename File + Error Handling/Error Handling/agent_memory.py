import json

class AgentMemoryError(Exception):
    def __init__(self,message=None):
        if message is None:
            print("An error has ocuured in Agent memory")
        else:
            print(message)

    def clear(self):
        print("Agent Memory cleared")

def save_agent_memory(memory,file):
    if type(memory) == dict:
        with open(file,'a') as f:
            json.dump(memory,f)
    else:
        raise AgentMemoryError('The memeory is not correct json')
    
    if memory == {}:
        raise AgentMemoryError


save_agent_memory([{'name':'xyz','age':22},10],'demo.json')
    
    
