from typing import Type

from coin import Coin


class CoinConvert:
    def convert(self, coin: Coin, coin_typ: Type[Coin]) -> Coin:
        ...
