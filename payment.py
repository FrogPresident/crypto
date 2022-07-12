import wallet
import user


class Payment:
    user: user.User
    wallet: wallet.Wallet

    def pay(self, money):
        ...


class BindablePayment(Payment):

    def get_identifier(self) -> str:
        ...


class BankAccount(BindablePayment):

    def pay(self, money):
        self.wallet.bound_payments[self.get_identifier()] = self
        print("Bank Success~~")
        print(f"total: {money}")
        return self.wallet.bound_payments[self.get_identifier()]

    def get_identifier(self) -> str:
        number = input("enter your bank account")
        return number
