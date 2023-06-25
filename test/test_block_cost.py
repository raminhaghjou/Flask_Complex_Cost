import pytest
from importlib.machinery import SourceFileLoader
b = SourceFileLoader('block_cost', 'BuildingCost/block_cost').load_module

# import sys
# sys.path.append('BuildingCost')
# import block_cost
# from block_cost import BlockCost
# from BuildingCost.block_cost import BlockCost

class TestBlock():
    @pytest.fixture()
    def input_value():
        value = 20000
        return value
    
    @pytest.fixture()
    def input_index():
        index = 1
        return index
        
    @pytest.fixture()
    def inst():
        block = b.BlockCost(1)
        return  block
    
    # def test_set_item(self,setup):
    #     assert 20000 in b.BlockCost().set_item(self.value[0])
        
    # @pytest.mark.parametrize('index', [1,2,3,4,5])
    def test_del_item(self, inst, input_index):
        with pytest.raises(ValueError) as exc:
            inst.__delitem__(input_index)
        assert (str(exc.value) == "Index out of range")
        
    # @pytest.mark.parametrize('value', [1,2,3,4,5])
    def test_set_item(self, input_value, inst):
        assert inst.set_item(input_value)!= None
        
    # @pytest.mark.parametrize('index, value', [1,2,3,4,5])
    def test__setitem__for_if_value_less_than_zero(self, inst, input_index, input_value):
        assert inst.__setitem__(input_index, input_value) != None