from enum import Enum
class Updates(Enum):
    #No Changes
    NONE = 0
    #Time Update
    TIME = 1
    #Producer Update
    PRODUCER = 2
    #Consumer Update
    CONSUMER = 3
    #Process Finishd
    END = 4