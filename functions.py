def add(a, b):
    """Add two numbers."""
    return a + b

def minus(a, b):
    """Subtract b from a."""
    return a - b

def gcd(a, b):
    while b:
        a, b = b, a % b  # b가 0이 될 때까지 a와 b를 나누며 반복
    return a