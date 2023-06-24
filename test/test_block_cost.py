import pytest
from importlib.machinery import SourceFileLoader
b = SourceFileLoader('block_cost', 'BuildingCost/block_cost').load_module

# import sys
# sys.path.append('BuildingCost')
# import block_cost
# from block_cost import BlockCost
# from BuildingCost.block_cost import BlockCost

class TestBlock():
    @pytest.fixture
    def setup(self):
        self.block = b.BlockCost(1)
        self.value = [20000, 50000]
        self.block = self.value
        self.index = [1, 2, 3, 4, 5, 6, 7]
    
    # def test_set_item(self,setup):
    #     assert 20000 in b.BlockCost().set_item(self.value[0])
        
    @pytest.mark.parametrize('index', [1,2,3,4,5])
    def test_del_item(self, index, setup):
        with pytest.raises(ValueError) as exc:
            self.block.__delitem__(index)
        assert (str(exc.value) == "Index out of range")
        
    @pytest.mark.parametrize('value', [1,2,3,4,5])
    def test_set_item(self):
        assert self.block.set_item(value)
        
    @pytest.mark.parametrize('index, value', [1,2,3,4,5])
    def test__setitem__for_if_value_less_than_zero(self):
        assert self.block.__setitem__(self.index, self.value) != None