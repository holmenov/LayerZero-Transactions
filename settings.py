from classes.Chains import Networks


# ==========================================================
#                       MAIN SETTINGS
# ==========================================================


class MainSettings:
    # Gwei control
    MAX_GAS = 80
    
    # Take the wallets in random order
    RANDOM_WALLETS = True 

    # Remove wallet from files after work
    REMOVE_WALLET = True

    # Proxy mode
    USE_PROXY = True

    # Period in seconds to run all wallets
    START_PERIOD_FROM = 1
    START_PERIOD_TO = 270

    # Module repetitions for each wallet
    REPEATS_PER_WALLET = 15

    # Sleeps after work
    SLEEP_AFTER_WORK_FROM = 5 # Seconds
    SLEEP_AFTER_WORK_TO = 20 # Seconds

    # Blockchain sender
    SEND_FROM = Networks.Polygon # Networks.(Chain) in Chain insert your chain
    
    # Withdraw from OKX before work
    OKX_WITHDRAW = False


# =================================================================
#                       OKX WITHDRAW SETTINGS
# =================================================================


class OKXSettings:
    # You can find this data when withdrawing funds to OKX
    SYMBOL = 'MATIC'
    CHAIN = 'Polygon'
    FEE = 0.1
    
    # Withdrawal amount
    AMOUNT_FROM = 1.7
    AMOUNT_TO = 2
    

    # Here you can get your api-key: https://www.okx.cab/ru/account/my-api
    SECRET_KEY = 'key'
    API_KEY = 'api'
    PASSPHRASE = 'passphrase'
    

# ===========================================================
#                       ROUTES SETTINGS
# ===========================================================


class RoutesSettings:

    class General:
        MIN_AMOUNT = 0.01
        MAX_AMOUNT = 0.02
        DECIMAL = 4
        USE_GENERAL_SETTINGS = True

    class Arbitrum:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class ArbitrumNova:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Optimism:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class ZkSync:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class PolygonZkEvm:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Zora:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Scroll:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Polygon:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Moonbeam:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Moonriver:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Canto:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Harmony:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Kava:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Conflux:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Gnosis:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Coredao:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Fuse:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Klaytn:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Dfk:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Orderly:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False