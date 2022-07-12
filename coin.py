class Coin:
    coin_name: str = ""
    value: float = 0

    quantity: float

    def __init__(self, quantity: float):
        self.quantity = quantity

    def __str__(self) -> str:
        return f'{self.coin_name}({self.quantity:.6f})'

    __repr__ = __str__


class BTC(Coin):
    coin_name = "BTC"
    value = 20390.5


class TWD(Coin):
    coin_name = "TWD"
    value = 0.034
