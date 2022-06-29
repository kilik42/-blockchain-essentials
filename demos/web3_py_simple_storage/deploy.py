from solx import compile_standard
from solx import deploy_contract
import json

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
