import random

from modules.merkly import Merkly
from modules.okx_withdraw import OKXWithdraw
from classes.Chains import DestinationChains
from settings import RoutesSettings as rs
from settings import MainSettings as SETTINGS


async def random_route(account_id: int, key: str, proxy: str):
    routes = {
        'Arbitrum': bridge_arbitrum,
        'ArbitrumNova': bridge_arbitrum_nova,
        'Optimism': bridge_optimism,
        'ZkSync': bridge_zksync,
        'PolygonZkEvm': bridge_polygon_zkevm,
        'Zora': bridge_zora,
        'Scroll': bridge_scroll,
        'Polygon': bridge_polygon,
        'Moonbeam': bridge_moonbeam,
        'Moonriver': bridge_moonriver,
        'Canto': bridge_canto,
        'Harmony': bridge_harmony,
        'Kava': bridge_kava,
        'Conflux': bridge_conflux,
        'Gnosis': bridge_gnosis,
        'Coredao': bridge_coredao,
        'Fuse': bridge_fuse,
        'Klaytn': bridge_klaytn,
        'Dfk': bridge_dfk,
        'Orderly': bridge_orderly
    }

    random_routes = [route for name, route in routes.items() if getattr(rs, name).USE_IN_RANDOM]

    choice = random.choice(random_routes)
    await choice(account_id, key, proxy)


async def okx_withdraw(account_id: int, key: str, proxy: str):
    okx_withdraw = OKXWithdraw(account_id, key)
    await okx_withdraw.withdraw()


async def bridge_route(route, account_id: int, key: str, proxy: str):
    if rs.General.USE_GENERAL_SETTINGS:
        min_amount = rs.General.MIN_AMOUNT
        max_amount = rs.General.MAX_AMOUNT
        decimal = rs.General.DECIMAL
    else:
        min_amount = getattr(rs, route).MIN_AMOUNT
        max_amount = getattr(rs, route).MAX_AMOUNT
        decimal = getattr(rs, route).DECIMAL

    token = SETTINGS.SEND_FROM.token

    merkly_refuel = Merkly(account_id, key, proxy, getattr(DestinationChains, route))
    return await merkly_refuel.merkly_refuel(min_amount, max_amount, decimal, token)


async def bridge_arbitrum(account_id: int, key: str, proxy: str):
    return await bridge_route('Arbitrum', account_id, key, proxy)


async def bridge_arbitrum_nova(account_id: int, key: str, proxy: str):
    return await bridge_route('ArbitrumNova', account_id, key, proxy)


async def bridge_optimism(account_id: int, key: str, proxy: str):
    return await bridge_route('Optimism', account_id, key, proxy)


async def bridge_zksync(account_id: int, key: str, proxy: str):
    return await bridge_route('ZkSync', account_id, key, proxy)


async def bridge_polygon_zkevm(account_id: int, key: str, proxy: str):
    return await bridge_route('PolygonZkEvm', account_id, key, proxy)


async def bridge_zora(account_id: int, key: str, proxy: str):
    return await bridge_route('Zora', account_id, key, proxy)


async def bridge_scroll(account_id: int, key: str, proxy: str):
    return await bridge_route('Scroll', account_id, key, proxy)


async def bridge_polygon(account_id: int, key: str, proxy: str):
    return await bridge_route('Polygon', account_id, key, proxy)


async def bridge_moonbeam(account_id: int, key: str, proxy: str):
    return await bridge_route('Moonbeam', account_id, key, proxy)


async def bridge_moonriver(account_id: int, key: str, proxy: str):
    return await bridge_route('Moonriver', account_id, key, proxy)


async def bridge_canto(account_id: int, key: str, proxy: str):
    return await bridge_route('Canto', account_id, key, proxy)


async def bridge_harmony(account_id: int, key: str, proxy: str):
    return await bridge_route('Harmony', account_id, key, proxy)


async def bridge_kava(account_id: int, key: str, proxy: str):
    return await bridge_route('Kava', account_id, key, proxy)


async def bridge_conflux(account_id: int, key: str, proxy: str):
    return await bridge_route('Conflux', account_id, key, proxy)


async def bridge_gnosis(account_id: int, key: str, proxy: str):
    return await bridge_route('Gnosis', account_id, key, proxy)


async def bridge_coredao(account_id: int, key: str, proxy: str):
    return await bridge_route('Coredao', account_id, key, proxy)


async def bridge_fuse(account_id: int, key: str, proxy: str):
    return await bridge_route('Fuse', account_id, key, proxy)


async def bridge_klaytn(account_id: int, key: str, proxy: str):
    return await bridge_route('Klaytn', account_id, key, proxy)


async def bridge_dfk(account_id: int, key: str, proxy: str):
    return await bridge_route('Dfk', account_id, key, proxy)


async def bridge_orderly(account_id: int, key: str, proxy: str):
    return await bridge_route('Orderly', account_id, key, proxy)