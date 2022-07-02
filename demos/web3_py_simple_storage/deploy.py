from solcx import compile_standard, install_solc

install_solc("0.6.0")
from solcx import deploy_contract
import json
import os
from dotenv import load_dotenv

load_dotenv()

# from dotenv import load_dotenv
from web3 import Web3

with open("./simple_storage.sol", "r") as f:
    simple_storage_file = f.read

# compile our solidity code

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simple_storage": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata" "evm.bytecode.object", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
print(compiled_sol)
with open("compiled_code.json", "w") as file:
    json.dump(compiled - sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

print(abi)
# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))

# you will need the chain id as well
chainId = 5777
address = "0x4600a0B9525C7d7DBe50F1439A3ef502f74f3Ed2"
private_key = os.getenv("PRIVATE_KEY")

# deploy contract
SimpleStorage = w3.eth.contract(abi=abi, bytcode=bytecode)
print(SimpleStorage)

# 1 build the contract deploy transaction
# 2 sign the transaction
# 3 send the transaction

# understanding nonce.
# get the latest transaction/build it
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)
print(transaction)

# now we need to sign it
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

print(signed_txn)
# send this signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# working with contract
# need address and abi

simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

print(simple_storage.functions.retrieve().call())
print(simple_storage.functions.store(15).call())

# creat a transaction to store the value
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)

# sign the transaction
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)

# send the transaction
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
