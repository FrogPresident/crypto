from typing import Type

from coin import TWD, Coin
import wallet


class User:
    default_coin_typ: Type[Coin] = TWD
    wallet: wallet.Wallet

    def __init__(self):
        self.wallet = wallet.Wallet(self)
