import block
import time

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis()]

    def create_genesis(self):
        trans = block.Transaction("0", "0", 0)
        return block.Block(trans, "0", time.time())

bc = BlockChain()

print(bc.chain[0].hash)