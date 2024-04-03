import random

def generate_random_number(start, end):
    return random.randint(start, end)

# Example usage:
random_number = generate_random_number(1, 100)
print("Random number:", random_number)
