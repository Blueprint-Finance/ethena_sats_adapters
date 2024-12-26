import json
from web3 import Web3
from utils.web3_utils import w3

#TODO: Add the addresses

PAGINATION_SIZE = 2000
CONCRETE_START_BLOCK = 21202656
CONCRETE_USDCE_ADDRESS = Web3.to_checksum_address("")
CONCRETE_SUSDCE_ADDRESS = Web3.to_checksum_address("")
with open("abi/concrete_vault.json") as f:
    VAULT_ABI = json.load(f)

USDCE_CONTRACT = w3.eth.contract(
    address=CONCRETE_USDCE_ADDRESS,
    abi=VAULT_ABI,
)
SUSDC_CONTRACT = w3.eth.contract(
    address=CONCRETE_SUSDCE_ADDRESS,
    abi=VAULT_ABI,
)

