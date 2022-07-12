class Payment:

    def pay(self, money):
        ...


class BindablePayment(Payment):

    def get_identifier(self) -> str:
        ...


class BankAccount(BindablePayment):

    def pay(self, money):
        print("Bank pay Success~~")
        print(f"total: {money}")

    def get_identifier(self) -> str:
        number = input("enter your bank account")
        return number
