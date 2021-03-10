import block
import time

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis()]
        self.pending_transactions = []

    def create_genesis(self):
        trans = block.Transaction("0", "0", 0)
        return block.Block(trans, "0", time.time())

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

bc = BlockChain()

bc.add_transaction(block.Transaction("nate", "bob", 100))
bc.add_transaction(block.Transaction("bob", "nate", 50))
