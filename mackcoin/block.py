import hashlib
import json
import time

class Block:
    def __init__(self, transactions, prev_hash, timestamp):
        self.prev_hash = prev_hash
        self.transactions = transactions.copy()
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):

        temp_str = "{}{}{}{}".format(json.dumps(self.transactions), self.prev_hash, self.nonce, self.timestamp)
        return hashlib.sha256(temp_str.encode()).hexdigest()

    def mine_block(self):
        while(self.hash[0:5] != "00000"):
            self.nonce += 1
            self.hash = self.calc_hash()
            
        print("Block successfully mined.")

        
    

"""
This class defines the structure for a transaction.
"""
class Transaction:
    def __init__(self, to_address, from_address, amount):
        self.to_address = to_address
        self.from_address = from_address
        self.amount = amount


