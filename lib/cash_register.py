#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Set up the cash register
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # Add the item's price to the total
        self.total = self.total + (price * quantity)

        # Add the item to the list for each quantity
        for i in range(quantity):
            self.items.append(item)

        # Save the transaction so it can be voided later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Tell the user if there is no discount
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Calculate the discounted total
            self.total = self.total - (self.total * self.discount / 100)
            self.total = int(self.total)

            # Show the new total
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        # Remove the most recent transaction
        if len(self.previous_transactions) > 0:
            transaction = self.previous_transactions.pop()

            # Subtract the transaction from the total
            self.total = self.total - (transaction["price"] * transaction["quantity"])

            # Remove the items from the items list
            for i in range(transaction["quantity"]):
                self.items.remove(transaction["item"])