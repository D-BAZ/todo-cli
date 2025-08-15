import os
import json
from todo_cli.status import *
from typing_extensions import Annotated

def try_read():
    try:  
        with open("./tasks.json", "r") as file:
            data = json.load(file)["tasks"]

    except (FileNotFoundError , TypeError , json.decoder.JSONDecodeError):
        print(f"Json file not found, creating one")
        default_state ={"tasks":[]}
        with open("./tasks.json", "w") as file:
            json.dump(default_state,file)
        data = try_read()
        
        
    return data

def write(data):
    with open("./tasks.json", "w") as file:
        data = {"tasks":data}
        json.dump(data,file)



if __name__ == "__main__":
    print("hi")
    