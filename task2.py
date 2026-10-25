import random

def get_numbers_ticket(min, max, quantity):
    """Generate a sorted list of unique random numbers within a given range."""
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > max - min + 1:
        return []

    random_numbers = random.sample(range(min, max + 1), quantity)
    random_numbers.sort()
    return random_numbers


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(0, 49, 6))
print(get_numbers_ticket(1, 1001, 6))
print(get_numbers_ticket(40, 49, 15))
print(get_numbers_ticket(50, 10, 5))
print(get_numbers_ticket(1, 5, 0))