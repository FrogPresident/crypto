import user
from coin import Coin, BTC, TWD
from payment import BankAccount


def main():
    frogboy69 = user.User()
    frogboy69.wallet.buy_coin(BTC(1), BankAccount())


if __name__ == '__main__':
    main()
