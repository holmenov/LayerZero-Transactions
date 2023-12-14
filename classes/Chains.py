from utils.config import MERKLY_CONTRACTS, CHAIN_IDS, RPC


class Networks:
    chain: str
    contract_address: str

    class Arbitrum:
        chain = 'arbitrum'
        contract_address = MERKLY_CONTRACTS[chain]
        token = RPC[chain]['token']

    class ArbitrumNova:
        chain = 'arbitrum-nova'
        contract_address = MERKLY_CONTRACTS[chain]
        token = RPC[chain]['token']

    class Optimism:
        chain = 'optimism'
        contract_address = MERKLY_CONTRACTS[chain]
        token = RPC[chain]['token']

    class ZkSync:
        chain = 'zksync'
        contract_address = MERKLY_CONTRACTS[chain]
        token = RPC[chain]['token']

    class PolygonZKevm:
        chain = 'polygon-zkevm'
        contract_address = MERKLY_CONTRACTS[chain]
        token = RPC[chain]['token']
    
    class Polygon:
        chain = 'polygon'
        contract_address = MERKLY_CONTRACTS[chain]
        token = RPC[chain]['token']


class DestinationChains:
    chain: str
    chainId: int

    class Arbitrum:
        chain = Networks.Arbitrum.chain
        chainId = CHAIN_IDS[chain]

    class ArbitrumNova:
        chain = Networks.ArbitrumNova.chain
        chainId = CHAIN_IDS[chain]

    class Optimism:
        chain = Networks.Optimism.chain
        chainId = CHAIN_IDS[chain]

    class ZkSync:
        chain = Networks.ZkSync.chain
        chainId = CHAIN_IDS[chain]

    class PolygonZKevm:
        chain = Networks.PolygonZKevm.chain
        chainId = CHAIN_IDS[chain]

    class Zora:
        chain = 'zora'
        chainId = CHAIN_IDS[chain]

    class Scroll:
        chain = 'scroll'
        chainId = CHAIN_IDS[chain]

    class Polygon:
        chain = 'polygon'
        chainId = CHAIN_IDS[chain]

    class Moonbeam:
        chain = 'moonbeam'
        chainId = CHAIN_IDS[chain]

    class Moonriver:
        chain = 'moonriver'
        chainId = CHAIN_IDS[chain]

    class Canto:
        chain = 'canto'
        chainId = CHAIN_IDS[chain]

    class Harmony:
        chain = 'harmony'
        chainId = CHAIN_IDS[chain]

    class Kava:
        chain = 'kava'
        chainId = CHAIN_IDS[chain]

    class Conflux:
        chain = 'conflux'
        chainId = CHAIN_IDS[chain]

    class Gnosis:
        chain = 'gnosis'
        chainId = CHAIN_IDS[chain]

    class Coredao:
        chain = 'coredao'
        chainId = CHAIN_IDS[chain]

    class Fuse:
        chain = 'fuse'
        chainId = CHAIN_IDS[chain]

    class Klaytn:
        chain = 'klaytn'
        chainId = CHAIN_IDS[chain]

    class Dfk:
        chain = 'dfk'
        chainId = CHAIN_IDS[chain]

    class Orderly:
        chain = 'orderly'
        chainId = CHAIN_IDS[chain]