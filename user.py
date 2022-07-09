from typing import Type

from coin import TWD, Coin


class User:
    default_coin_typ: Type[Coin] = TWD
