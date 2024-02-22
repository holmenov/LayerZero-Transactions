from loguru import logger
from classes.Account import Account
from modules.okx_withdraw import OKXWithdraw
from settings import MainSettings as SETTINGS


class OKXTopUp(Account):
    def __init__(self, account_id: int, private_key: str, proxy: str | None) -> None:
        super().__init__(account_id=account_id, private_key=private_key, proxy=proxy, chain=SETTINGS.SEND_FROM.chain)
    
    async def calculate_amount(self, min_balance: float, max_balance: float, decimals: int):
        amt_wei, amt, balance_wei = await self.get_amount(min_balance, max_balance, decimals)
        
        if amt_wei > balance_wei:
            required_balance_wei = amt_wei - balance_wei
            required_balance_eth = round(self.wei_to_eth(required_balance_wei), decimals)
            return required_balance_eth

        else:
            logger.success(f'Account №{self.account_id} | {self.address} | The account already has the requested balance: {round(self.wei_to_eth(balance_wei), 4)}!')
            return False
    
    async def okx_withdraw(self, account_id: int, key: str, amount_withdraw: float):
        okx_withdraw = OKXWithdraw(account_id, key)
        return await okx_withdraw.withdraw(amount_withdraw)
    
    async def top_up_balance(self, min_balance: float, max_balance: float, decimals: int):
        required_balance_eth = await self.calculate_amount(min_balance, max_balance, decimals)
        
        if required_balance_eth:
            return await self.okx_withdraw(self.account_id, self.private_key, required_balance_eth)
        
        else:
            return 'Filled'