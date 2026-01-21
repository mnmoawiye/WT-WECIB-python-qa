def withdraw(balance, amount):
    assert balance >= 0, "Balance cannot be negative"
    assert amount >= 0, "Withdrawal amount cannot be negative"

    if amount > balance:
        return balance
    return balance - amount
