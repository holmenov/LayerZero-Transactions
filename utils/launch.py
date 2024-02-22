import asyncio
from typing import Callable

from utils.utils import async_sleep, okx_withdraw, remove_wallet_from_files
from settings import MainSettings as SETTINGS
from utils.wrappers import repeats


async def start_tasks(module: Callable, data: list):
    tasks = []

    for account in data:
        tasks.append(
            asyncio.create_task(_run_module(module, account.get('id'), account.get('key'), account.get('proxy')))
        )

    await asyncio.gather(*tasks)


async def _run_module(module: Callable, account_id: int, key: str, proxy: str):
    await async_sleep(
        SETTINGS.START_PERIOD_FROM, SETTINGS.START_PERIOD_TO,
        True, account_id, key, 'before starting work'
    )

    if SETTINGS.OKX_WITHDRAW or SETTINGS.OKX_TOP_UP:
        success = await okx_withdraw(account_id, key, proxy)
        if not success: return False

    await run_module(module, account_id, key, proxy)

    if SETTINGS.REMOVE_WALLET:
        remove_wallet_from_files(key, proxy)


@repeats
async def run_module(module: Callable, account_id: int, key: str, proxy: str):
    succcess_bridge = await module(account_id, key, proxy)
    if not succcess_bridge: return False
    return True