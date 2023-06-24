from BuildingCost.block_cost import BlockCost

block = BlockCost(1)

block[0] = 20000

block.set_item(50000)

print(block)