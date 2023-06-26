from abc import ABC, abstractmethod

class Cost(ABC):
    def __init__(self, cost_for):
        self.cost_for = cost_for
        
    @abstractmethod
    def __setitem__(self, index, value):
        pass
    
    # @abstractmethod
    # def __getitem__(self, index):
    #     pass
    
    # @abstractmethod
    # def __delitem__(self, index):
    #     pass
    
    def set_item(self, value):
        pass
