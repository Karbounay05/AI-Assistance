# domain.pyx - simplified

def greet(str name):
    return f"Hello, {name}!"

def factorial(int n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def reverse_string(str s):
    return s[::-1]
