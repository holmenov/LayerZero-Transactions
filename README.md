![LayerZero](https://i.imgur.com/rX6SXJ0.png)

---

With this repository you will be able to send transactions to **Merkly** interacting with the **LayerZero** protocol.

Transactions are created through the gas delivery function in blockchains that support the **LayerZero** protocol.

Transactions are only sent from **Polygon, Arbitrum, Arbitrum-Nova, Optimism, ZkSync, PolygonZKEvm** to some of the cheapest blockchains such as: **Arbitrum Nova, Zora, Scroll, Polygon, Moonbeam, Moonriver, Canto, Harmony** and others.

You can also enable random choice routes to do random activity on LayerZero for your accounts.

There is also a module in the software that supports balance output to wallets from OKX exchange.

## INSTALLATION

1. Install **Python 3.11+**.
2. `git clone https://github.com/holmenov/LayerZero-Transactions.git`.
3. `cd LayerZero-Transactions`.
4. `pip install -r requirements.txt`.
5. Paste your proxies into `proxy.txt` in `ip:port@login:password` format
6. Paste the wallet private key in `accounts.txt`.
7. Set the settings in `settings.py`.

## GENERAL SETTINGS

- `MAX_GAS` - Maximum GAS in GWEI for transactions [Integer].
- `RANDOM_WALLET` - Random wallet mode [Boolean].
- `REMOVE_WALLET` - Remove wallet after work [Boolean].
- `USE_PROXY` - Proxy mode [Boolean].
- `START_PERIOD_FROM`, `START_PERIOD_TO` - Period in seconds to run all wallets [Integer].
- `REPEATS_PER_WALLET` - Module repetitions for each wallet [Integer].
- `SLEEP_AFTER_WORK_FROM`, `SLEEP_AFTER_WORK_TO` - Seconds to sleep after completing a task [Integer].
- `SEND_FROM` - Blockchain sender [Class].
- `OKX_WITHDRAW` - Withdraw from OKX before work [Boolean].

## OKX WITHDRAW SETTINGS

Get the secret key, api key and passphrase at: **https://www.okx.cab/ru/account/my-api**.

**You also need to add your wallets to the whitelist on OKX!**

- `SYMBOL` - Token symbol [String].
- `CHAIN` - Chain to withdraw [String].
- `FEE` - Withdrawal Fee. You can look at OKX [Float].
- `AMOUNT_FROM`, `AMOUNT_TO` - A random sum in this interval will be generated [Float].
- `SECRET_KEY` - Your secret key [String].
- `API_KEY` - Your api-key [String].
- `PASSPHRASE` - Your passphrase [Float].

## ROUTES SETTINGS

In the General class, you can set general settings for all routes. Remember to set `USE_GENERAL_SETTINGS` to **True**.

Or you can set separate settings for each module, then you need to set `USE_GENERAL_SETTINGS` to **False** and set the settings for each module.

- `MIN_AMOUNT`, `MAX_AMOUNT` - Minimum and maximum amount. Set the amount in the token of the network you want to send from, e.g. ETH for Arbitrum or MATIC for Polygon.
- `DECIMAL` - Number of decimal places to generate a random amount.
- `USE_IN_RANDOM` - Set `True` if you want to use this route in the random routes function or `False` if you do not want to use this route in random routes.