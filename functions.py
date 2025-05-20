def calculate_average(numbers):
    if len(numbers) == 0:
        return None  # 또는 0, 혹은 예외 발생
    return sum(numbers) / len(numbers)


def add(a, b):
    """Add two numbers."""
    return a + b

def minus(a, b):
    """Subtract b from a."""
    return a - b
