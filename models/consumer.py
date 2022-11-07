class Consumer:
    def __init__(self) -> None:
        self._sleep = True # Sleep state
        self._remainingTime = 0 # Remaining time to wake up
        self._available = False #True = Productos Disponible, False = Productos Ocupado
        self._consumeItems = 0 # Number of items to consume
        self._lasItemIndx = 0 # Last item index
    
    def isSleeping(self) -> bool:
        return self._sleep
    
    def getRemainingTime(self) -> int:
        return self._remainingTime
    
    def getConsumeItems(self) -> int:
        return self._consumeItems

    def getLastItemIndex(self) -> int:
        return self._lasItemIndx
    
    def isAvailable(self) -> bool:
        return self._available
    
    def setSleep(self, sleep: bool) -> None:
        self._sleep = sleep
    
    def setRemainingTime(self, remainingTime: int) -> None:
        self._remainingTime = remainingTime
    
    def setConsumeItems(self, consumeItems: int) -> None:
        self._consumeItems = consumeItems
    
    def setAvailability(self, available: bool) -> None:
        self._available = available
        
    def setLastItemIndex(self, lastItemIndex: int) -> None:
        self._lasItemIndx = lastItemIndex
        
    def update(self):
        if(self._sleep):
            self._remainingTime -= 1
            if(self._remainingTime == 0):
                self._sleep = False
                self._available = True
        else:
            if(self._consumeItems > 0):
                self._consumeItems -= 1
                self._lasItemIndx += 1
                if(self._lasItemIndx == 25):
                    self._lasItemIndx = 0
            else:
                self._sleep = True
                self._available = False