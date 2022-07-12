import user
from coin import BTC
from payment import BankAccount


def main():
    frogboy69 = user.User()
    frogboy69.wallet.buy_coin(BTC(2), BankAccount())
    frogboy69.wallet.buy_coin(BTC(1), BankAccount())
    print(frogboy69.wallet.own_coins)


if __name__ == '__main__':
    main()
