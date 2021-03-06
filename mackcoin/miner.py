import blockchain
import block
import time

class Miner:
    def __init__(self, block_chain, miner_address):
        self.bc = block_chain
        self.miner_address = miner_address

    def mine_pending_transactions(self):
        start_time = time.time()

        self.blk = block.Block(self.bc.pending_transactions , self.bc.chain[-1].hash, time.time())
        self.blk.mine_block()

        print("\nNew block mined")
        print(self.blk.__dict__)
        print("\nMining finished in {:.2f} seconds".format(time.time() - start_time))
        print(str(self.miner_address) + " has recieved 1 coin")
        self.bc.add_block(self.blk)
        self.bc.clear_pending_transactions()
        self.bc.add_transaction(block.Transaction(self.miner_address, 'null', 1))

