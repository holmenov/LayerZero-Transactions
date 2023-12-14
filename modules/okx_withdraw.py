import base64
from datetime import datetime
import hmac
import random
import aiohttp
import ccxt
import eth_account
from loguru import logger

from settings import OKXSettings


class OKXWithdraw:
    def __init__(self, account_id: int, private_key: str) -> None:
        self.symbol = OKXSettings.SYMBOL
        self.amount = round(random.uniform(OKXSettings.AMOUNT_FROM, OKXSettings.AMOUNT_TO), 4)
        self.fee = OKXSettings.FEE
        self.chain = OKXSettings.CHAIN
        self.api_key = OKXSettings.API_KEY
        self.secret_key = OKXSettings.SECRET_KEY
        self.passphrase = OKXSettings.PASSPHRASE
        self.dest = 4
        
        self.account_id = account_id
        self.address = eth_account.Account.from_key(private_key).address
    
    async def make_http_request(self, url, method, headers=None, params=None, data=None, timeout=10):
        async with aiohttp.ClientSession() as session:
            kwargs = {"url": url, "method": method, "timeout": timeout}
                
            if headers:
                kwargs["headers"] = headers
            
            if params:
                kwargs["params"] = params
            
            if data:
                kwargs["data"] = data
            
            async with session.request(**kwargs) as response:
                return await response.json()

    async def get_data(self, request_path, body, method):
        def signature(timestamp: str, method: str, request_path: str, secret_key: str, body: str):
            message = timestamp + method.upper() + request_path + body
            mac = hmac.new(
                bytes(secret_key, encoding="utf-8"),
                bytes(message, encoding="utf-8"),
                digestmod="sha256",
            )
            d = mac.digest()
            return base64.b64encode(d).decode("utf-8")

        dt_now = datetime.utcnow()
        ms = str(dt_now.microsecond).zfill(6)[:3]
        timestamp = f"{dt_now:%Y-%m-%dT%H:%M:%S}.{ms}Z"

        headers = {
            "Content-Type": "application/json",
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-SIGN": signature(timestamp, method, request_path, self.secret_key, body),
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": self.passphrase,
            'x-simulated-trading': '0'
        }

        return headers

    async def withdraw(self):
        try:
            body = {
                "ccy": self.symbol,
                "amt": self.amount,
                "fee": self.fee,
                "dest": self.dest,
                "chain": f"{self.symbol}-{self.chain}",
                "toAddr": self.address
            }

            headers = await self.get_data(request_path='/api/v5/asset/withdrawal', method='POST', body=str(body))
            result = await self.make_http_request("https://www.okx.cab/api/v5/asset/withdrawal",data=str(body), method="POST", headers=headers)

            if result['code'] == '0':
                logger.success(f'Account №{self.account_id} | {self.address} | Successfully withdraw {self.amount} {self.symbol} from OKX.')
                return True
            else:
                e = result['msg']
                logger.error(f'Account №{self.account_id} | {self.address} | Error occurred when withdraw {self.amount} {self.symbol} with OKX: {e}')
                return False

        except Exception as e:
            logger.error(f'Account №{self.account_id} | {self.address} | Error occurred when withdraw {self.amount} {self.symbol} with OKX: {e}')
            return False