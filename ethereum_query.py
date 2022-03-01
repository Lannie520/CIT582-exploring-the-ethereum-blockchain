from web3 import Web3
from hexbytes import HexBytes
import binascii


IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
# #     This line will mess with our autograders, but might be useful when debugging
# #     print( "Connected to Ethereum node" )
# else:
#     print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    tx = w3.eth.getTransaction(tx)   #YOUR CODE HERE
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    gas_price = get_transaction(tx)["gasPrice"] #YOUR CODE HERE
    return gas_price

def get_gas(tx):
    gas = w3.eth.get_transaction_receipt(tx)["gasUsed"] #YOUR CODE HERE
    return gas

def get_transaction_cost(tx):

    price = get_gas_price(tx)
    num_gas = get_gas(tx)
    tx_cost = price * num_gas #YOUR CODE HERE
    return tx_cost

def get_block_cost(block_num):
    block_cost = 0  #YOUR CODE HERE
    count = w3.eth.get_block_transaction_count(block_num)

    for t in range(0, count):
        tx = w3.eth.getTransactionByBlock(block_num,t).hash
        c = get_transaction_cost(tx)
        block_cost += c

    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    #max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')
    max_tx = w3.eth.getTransactionByBlock(block_num, 0).hash    #YOUR CODE HERE
    count = w3.eth.get_block_transaction_count(block_num)
    for i in range(0, count):
        tx = w3.eth.getTransactionByBlock(block_num, i).hash
        c = get_transaction_cost(tx)

        if(get_transaction_cost(max_tx) < c):
            max_tx = tx

    return max_tx


cost = get_transaction_cost(0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578)
print(cost*(pow(10, -18))*1385.02)

block_fee = []
for block in range(10237100, 10237109+1):
    block_fee.append(get_block_cost(block))

average = (sum(block_fee)/len(block_fee))
print(average * pow(10, -18))

one_cost = get_block_cost(10237208)
print(one_cost * pow(10, -18) * 248.26 + (2 * 248.26))

expensive = get_most_expensive_transaction(10237208)
print(binascii.hexlify(expensive))


