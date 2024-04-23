def is_power_of_two(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

# Test cases
print(is_power_of_two(8))  # Output: True
print(is_power_of_two(6))  # Output: False

