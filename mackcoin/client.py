import blockchain
import block
import miner
import os


# Clear console
def clear_window():
    os.system('cls' if os.name=='nt' else 'clear')


in_command = ""

print("Initializing blockchain...")
bc = blockchain.BlockChain()

print('Enter "list" for a list of commands')

def list_commands():
    clear_window()
    print("*****Commands List*****")
    print("Exit: ext")
    print("Mine for coins: mine")
    print("Make transaction: transaction")
    print("Check balance: balance \n")

def make_transaction():
    clear_window()
    frm = input("Enter your ID: ")
    to = input("Enter recipients ID: ")
    amt = input("Enter amount: ")
    bc.add_transaction(block.Transaction(to, frm, int(amt)))
    clear_window()
    print("Transaction complete\n")

def mine_coins():
    clear_window()
    ad = input("Enter your ID: ")
    mn = miner.Miner(block_chain = bc, miner_address = ad)
    clear_window()
    print("Mining begun...")
    mn.mine_pending_transactions()

def check_balance():
    clear_window()
    ad = input("Enter your ID to check balance: ")
    print("Your balance is: " + str(bc.get_balance(ad)))


while(in_command != "ext"):
    in_command = input("Enter command: ")
    
    if in_command == "list":
        list_commands()
    elif in_command == "transaction":
        make_transaction()
    elif in_command == "mine":
        mine_coins()
    elif in_command == "balance":
        check_balance()
