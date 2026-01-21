def average(numbers):
    if len(numbers) == 0:
        return 0  # or return None, depending on requirements

    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
