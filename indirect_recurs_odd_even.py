def is_odd(num):
    return False if num == 0 else is_even(num - 1)

def is_even(num):
    return True if num == 0 else is_odd(num - 1)

num = 4
print(is_odd(num)) # False
print(is_even(num)) # True
