from typing import TYPE_CHECKING

from coin import Coin
from coin_convert import CoinConvert
from payment import Payment, BindablePayment

if TYPE_CHECKING:
    from user import User


class Wallet:
    own_coins: dict[str, Coin]
    bound_payments: dict[str, BindablePayment]
    converter = CoinConvert()

    user: "User"

    def __init__(self, user: "User"):
        self.user = user
        self.own_coins = {}
        self.bound_payments = {}

    def buy_coin(self, coin: Coin, _payment: Payment):
        convert_coin: Coin = self.converter.convert(coin, self.user.default_coin_typ)
        # add wallet instance to payment
        _payment.wallet = self
        _payment.pay(convert_coin.quantity)
        if coin.coin_name not in self.own_coins:
            self.own_coins[coin.coin_name] = type(coin)(0)
        self.own_coins[coin.coin_name].quantity += coin.quantity

    def bind_payment(self, _payment: BindablePayment):
        self.bound_payments[_payment.get_identifier()] = _payment
