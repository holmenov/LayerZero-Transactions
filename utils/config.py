import json

with open('data/rpc.json', 'r') as file:
    RPC = json.load(file)
    
with open('data/erc20_abi.json', 'r') as file:
    ERC20_ABI = json.load(file)
    
with open('accounts.txt', 'r') as file:
    ACCOUNTS = [row.strip() for row in file]
    
with open("proxy.txt", "r") as file:
    PROXIES = [row.strip() for row in file]
    
with open("data/merkly/abi.json", "r") as file:
    MERKLY_ABI = json.load(file)
    
with open("data/merkly/destination_chains.json", "r") as file:
    CHAIN_IDS = json.load(file)
    
with open("data/merkly/merkly_contracts.json", "r") as file:
    MERKLY_CONTRACTS = json.load(file)