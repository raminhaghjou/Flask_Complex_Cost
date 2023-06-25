import sys
sys.path.append('..')

import cost

class BlockCost(cost.Cost):
    def __init__(self, element=1):
        super().__init__("Block")
        self.cost_list = [None] * element
        
    def __str__(self):
        return str(list(self.cost_list))
    
    def __setitem__(self, index, value):
        if value > 0: self.cost_list[index] = value
        else: raise ValueError("Value must be positive")
        
    def __getitem__(self, index):
        return self.cost_list[index]
    
    def __delitem__(self, index):
        if index < len(self.cost_list): self.cost_list[index] = None  
        else: raise ValueError("Index out of range")
        
    def set_item(self, value):
        if value > 0 : return self.cost_list.append(value)
        else : raise ValueError("Value must be positive")