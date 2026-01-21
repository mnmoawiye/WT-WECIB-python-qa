def calculate_discount(price, is_member):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if is_member:
        return price * 0.90
    return price
