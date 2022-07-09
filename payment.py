class Payment:
    def pay(self, money):
        ...


class BindablePayment(Payment):
    def get_identifier(self) -> str:
        ...


class BankAccount(BindablePayment):
    def __init__(self, ...):
        ...
    def pay(self, money):
        print("Bank Success~~")
        print(f"total: {money}")

    def get_identifier(self) -> str:
        ...
