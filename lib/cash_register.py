#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total = self.total + (price * quantity)

        for i in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total - (self.total * self.discount / 100)
            self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) > 0:
            transaction = self.previous_transactions.pop()

            self.total = self.total - (transaction["price"] * transaction["quantity"])

            for i in range(transaction["quantity"]):
                self.items.remove(transaction["item"])