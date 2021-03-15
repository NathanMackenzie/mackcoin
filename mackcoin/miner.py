import blockchain
import block
import time

class Miner:
    def __init__(self, block_chain, miner_address):
        self.bc = block_chain
        self.miner_address = miner_address

    def mine_pending_transactions(self):
        start_time = time.time()
        print("Mining begun...")

        self.blk = block.Block(self.bc.pending_transactions , self.bc.chain[-1].hash, time.time())
        self.blk.mine_block()

        print("Mining finished in {:.2f} seconds".format(time.time() - start_time))
        print("New hash: " + self.blk.hash)

    def print_pending_transactions(self):
        for i in self.bc.pending_transactions:
            print("******Transaction*******")
            print(i)
