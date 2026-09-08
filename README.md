# Object Oriented Programming (OOP) Part 2 - Cash Register Lab

## Description

This project is a simple Cash Register built using Python and Object Oriented Programming.

The Cash Register can:

- Add items and prices to the total
- Add multiple quantities of an item
- Apply a percentage discount
- Keep track of previous transactions
- Void the last transaction

## CashRegister Class

The `CashRegister` class has the following attributes:

- `discount` - the percentage discount
- `total` - the current total price
- `items` - a list of items added
- `previous_transactions` - keeps track of transactions

### Methods

- `add_item(item, price, quantity)` - adds an item to the register
- `apply_discount()` - applies the discount to the total
- `void_last_transaction()` - removes the most recent transaction

## Testing

The project uses pytest for testing.

All tests are passing:

```text
14 passed