import hashlib
import time

class Block:
    def __init__(self, transactions, prev_hash, timestamp):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        temp_str = "{}{}{}{}".format(self.transactions, self.prev_hash, self.nonce, self.timestamp)
        return hashlib.sha256(temp_str.encode()).hexdigest()


bl = Block("1", "fdshsgh", time.time())
print(bl.hash)