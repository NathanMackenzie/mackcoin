import blockchain
import block
import miner

#Create new block chain
bc = blockchain.BlockChain()

#Add some transactions
bc.add_transaction(block.Transaction("nate", "bob", 100))
bc.add_transaction(block.Transaction("bob", "nate", 50))

#Create a miner
mn = miner.Miner(block_chain = bc, miner_address = 'nates-addess')

#Display pending transactions
mn.print_pending_transactions()

#Begin mining transactions
mn.mine_pending_transactions()