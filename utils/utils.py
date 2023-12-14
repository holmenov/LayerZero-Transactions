import asyncio
import random
import sys
from loguru import logger
import eth_account

from modules.okx_withdraw import OKXWithdraw
from utils.config import ACCOUNTS, PROXIES
from settings import MainSettings as SETTINGS


async def async_sleep(sleep_from: int, sleep_to: int, logs: bool = True, account_id: int = 0, key: str = '', msg: str = ''):
    delay = random.randint(sleep_from, sleep_to)
    
    if logs:
        if not msg:
            logger.info(f'Account №{account_id} | {get_wallet_address(key)} | Sleep {delay} seconds.')
        else:
            logger.info(f'Account №{account_id} | {get_wallet_address(key)} | Sleep {delay} seconds, {msg}.')

    for _ in range(delay): await asyncio.sleep(1)


async def okx_withdraw(account_id, key):
    okx = OKXWithdraw(account_id, key)
    withdraw_success = await okx.withdraw()

    if withdraw_success:
        await async_sleep(90, 150, True, account_id, key, 'waiting tokens to arrive on the wallet')
        return True
    else:
        logger.error(
            f'Account №{account_id} | {get_wallet_address(key)} | The withdrawal has not been created. Work with the account has been completed unsuccessfully.'
        )
        return False


def get_wallet_address(key: str) -> str:
    account = eth_account.Account.from_key(key)
    return account.address


def get_wallets():
    if SETTINGS.USE_PROXY and len(ACCOUNTS) != len(PROXIES):
        logger.error('The number of wallets and proxies does not match.')
        sys.exit()
    
    elif len(ACCOUNTS) < 1:
        logger.error('It seems you forgot to enter the wallets.')
        sys.exit()
    
    accounts_proxy = dict(zip(ACCOUNTS, PROXIES)) if SETTINGS.USE_PROXY else ACCOUNTS

    wallets = [
        {
            'id': _id,
            'key': key,
            'proxy': accounts_proxy[key] if SETTINGS.USE_PROXY else None
        } for _id, key in enumerate(accounts_proxy, start=1)
    ]

    return wallets


def remove_wallet_from_files(account_to_remove: str, proxy_to_remove: str):
    with open('accounts.txt', 'r', encoding='utf-8') as accounts_file:
        accounts = accounts_file.readlines()
    with open('proxy.txt', 'r', encoding='utf-8') as proxy_file:
        proxies = proxy_file.readlines()
    
    cleared_accounts = [account for account in accounts if account.strip() != account_to_remove]
    cleared_proxies = [proxy for proxy in proxies if proxy.strip() != proxy_to_remove]
    
    with open('accounts.txt', 'w', encoding='utf-8') as accounts_file:
        accounts_file.writelines(cleared_accounts)
    with open('proxy.txt', 'w', encoding='utf-8') as proxy_file:
        proxy_file.writelines(cleared_proxies)