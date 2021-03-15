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

    def add_block(self, block):
        self.chain.append(block)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction.__dict__)

    def clear_pending_transactions(self):
        self.pending_transactions.clear()

    def print_pending_transactions(self):
        for i in self.pending_transactions:
            print("******Transaction*******")
            print(i)

    def print_blockchain(self):
        for i in self.chain:
            print(i.__dict__)

    def get_balance(self, address):
        sum = 0
        for blk in self.chain:
            for trans in blk.transactions:
                if trans.get("to_address") == address:
                    sum += trans.get("amount")
                if trans.get("from_address") == address:
                    sum -= trans.get("amount")
        return sum

        

