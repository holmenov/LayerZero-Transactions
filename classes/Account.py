import asyncio
import random

import eth_account
from loguru import logger
from web3 import AsyncWeb3
from web3.types import TxParams

from utils.config import ERC20_ABI, RPC
from utils.utils import async_sleep


class Account:
    def __init__(self, account_id: int, private_key: str, chain: str, proxy: str | None) -> None:
        self.account_id = account_id
        self.private_key = private_key
        self.chain = chain
        self.explorer = RPC[chain]['explorer']
        self.token = RPC[chain]['token']
        
        self.request_kwargs = {'proxy': f'http://{proxy}'} if proxy else {}
            
        self.w3 = AsyncWeb3(
            AsyncWeb3.AsyncHTTPProvider(random.choice(RPC[chain]['rpc'])),
            request_kwargs=self.request_kwargs
        )

        self.address = eth_account.Account.from_key(private_key).address
    
    async def get_amount(self, min_amount: float, max_amount: float, decimal: int):
        balance = await self.w3.eth.get_balance(self.address)
        amount = round(random.uniform(min_amount, max_amount), decimal)
        amount_wei = self.w3.to_wei(amount, 'ether')
        
        return amount_wei, amount, balance
    
    def get_contract(self, contract_address: str, abi = None):
        contract_address = self.w3.to_checksum_address(contract_address)
        
        abi = ERC20_ABI if abi is None else abi
        
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        
        return contract
    
    async def get_tx_data(self, value: int = 0) -> dict:
        tx = {
            'chainId': await self.w3.eth.chain_id,
            'from': self.address,
            'value': value,
            'gasPrice': await self.w3.eth.gas_price,
            'nonce': await self.w3.eth.get_transaction_count(self.address)
        }
        return tx
    
    async def execute_transaction(self, tx: TxParams, wait_complete: bool = True):
        signed_tx = await self.sign(tx)
        tx_hash = await self.send_raw_transaction(signed_tx)

        if wait_complete:
            await self.wait_until_tx_finished(tx_hash)
        else:
            logger.success(f'{self.account_id} | {self.address} | The transaction has been sent!')
            return tx_hash
    
    async def sign(self, transaction):
        gas = await self.w3.eth.estimate_gas(transaction)
        
        transaction.update({'gas': gas})
        
        signed_tx = self.w3.eth.account.sign_transaction(transaction, self.private_key)
        return signed_tx
    
    async def send_raw_transaction(self, signed_txn):
        txn_hash = await self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return txn_hash

    async def wait_until_tx_finished(self, hash: str):
        ATTEMPTS = 12
        attempt_counter = 0
        
        while True:
            if attempt_counter == ATTEMPTS:
                return logger.error(f'{self.account_id} | {self.address} | {self.explorer}{hash.hex()} transaction not found!')

            try:
                receipts = await self.w3.eth.get_transaction_receipt(hash)
                status = receipts.get('status')

                if status == 1:
                    return logger.success(f'{self.account_id} | {self.address} | {self.explorer}{hash.hex()} successfully!')
                elif status is None:
                    await asyncio.sleep(1)
                else:
                    return logger.success(f'{self.account_id} | {self.address} | {self.explorer}{hash.hex()} transaction failed!')
            except Exception:
                await async_sleep(10, 10, False)
                attempt_counter += 1