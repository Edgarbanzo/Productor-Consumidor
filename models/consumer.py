class Consumer:
    def __init__(self) -> None:
        self._sleep = True # Sleep state
        self._remainingTime = 0 # Remaining time to wake up
        self._available = False #True = Productos Disponible, False = Productos Ocupado
        self._consumeItems = 0 # Number of items to consume
    
    def isSleep(self) -> bool:
        return self._sleep
    
    def getRemainingTime(self) -> int:
        return self._remainingTime
    
    def getConsumeItems(self) -> int:
        return self._consumeItems
    
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