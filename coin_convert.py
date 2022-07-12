from typing import Type

from coin import Coin


class CoinConvert:
    def convert(self, coin: Coin, coin_typ: Type[Coin]) -> Coin:
        return coin_typ((coin.value * coin.quantity) / coin_typ.value)
