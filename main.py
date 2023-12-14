import asyncio
from loguru import logger
import questionary

from utils.launch import start_tasks
from utils.routes import *
from utils.utils import get_wallets


def get_module():
    routes = [
        questionary.Choice('1) Random routes', random_route),
        questionary.Choice('2) OKX Withdraw', okx_withdraw),
        questionary.Choice('3) Merkly | Arbitrum Nova', bridge_arbitrum_nova), # 0.28$ - 40 GWEI
        questionary.Choice('4) Merkly | Zora', bridge_zora), # 0.18$ - 40 GWEI
        questionary.Choice('5) Merkly | Scroll', bridge_scroll), # 0.4$ - 40 GWEI
        questionary.Choice('6) Merkly | Polygon', bridge_polygon), # 0.38$ - 40 GWEI
        questionary.Choice('7) Merkly | Moonbeam', bridge_moonbeam), # 0.06$ - 40 GWEI
        questionary.Choice('8) Merkly | Moonriver', bridge_moonriver), # 0.06$ - 40 GWEI
        questionary.Choice('9) Merkly | Canto', bridge_canto), # 0.2$ - 40 GWEI
        questionary.Choice('10) Merkly | Harmony', bridge_harmony), # 0.05$ - 40 GWEI
        questionary.Choice('11) Merkly | Kava', bridge_kava), # 0.05$ - 40 GWEI
        questionary.Choice('12) Merkly | Conflux', bridge_conflux), # 0.05$ - 40 GWEI
        questionary.Choice('13) Merkly | Gnosis', bridge_gnosis), # 0.05$ - 40 GWEI
        questionary.Choice('14) Merkly | Coredao', bridge_coredao), # 0.05$ - 40 GWEI
        questionary.Choice('15) Merkly | Fuse', bridge_fuse), # 0.05$ - 40 GWEI
        questionary.Choice('16) Merkly | Klaytn', bridge_klaytn), # 0.05$ - 40 GWEI
        questionary.Choice('17) Merkly | Dfk', bridge_dfk), # 0.05$ - 40 GWEI
        questionary.Choice('18) Merkly | Orderly', bridge_orderly), # 0.05$ - 40 GWEI
    ]

    route = questionary.select(
        'Choose your route:',
        choices=routes,
        qmark='📌 ',
        pointer='➡️ '
    ).ask()

    return route

def main():
    module = get_module()
    data = get_wallets()

    asyncio.run(start_tasks(module, data))

if __name__ == '__main__':
    logger.add('logs.log')
    main()