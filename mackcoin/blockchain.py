import block
import time

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis()]
        self.pending_transactions = []

    def create_genesis(self):
        print("Creating genesis block...")
        trans = [block.Transaction("0", "0", 0).__dict__]
        gen_block = block.Block(trans, "0", time.time())
        print("Genesis block created. Hash: " + str(gen_block.hash))
        return gen_block

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction.__dict__)

