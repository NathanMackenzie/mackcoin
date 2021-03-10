import blockchain
import block
import miner

bc = blockchain.BlockChain()

bc.add_transaction(block.Transaction("nate", "bob", 100))
bc.add_transaction(block.Transaction("bob", "nate", 50))
