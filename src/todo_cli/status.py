from enum import Enum

class Status(str,Enum):
    TODO = "todo"
    INPROGRESS = "in-progress"
    DONE = "done"