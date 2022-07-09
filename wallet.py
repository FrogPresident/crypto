from typing import Type

from coin import Coin
from coin_convert import CoinConvert
from payment import Payment, BindablePayment
from user import User


class Wallet:
    own_coins: dict[str, Coin]
    bound_payments: dict[str, BindablePayment]
    converter = CoinConvert()

    user: User

    def __init__(self, user: User):
        self.user = user
        self.own_coins = {}
        self.bound_payments = {}

    def buy_coin(self, coin: Coin, payment: Payment):
        convert_coin: Coin = self.converter.convert(coin, self.user.default_coin_typ)
        payment.pay(convert_coin.quantity)
        if coin.coin_name not in self.own_coins:
            self.own_coins[coin.coin_name] = type(coin)(0)
        self.own_coins[coin.coin_name].quantity += coin.quantity
