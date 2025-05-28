# domain.pyx

def some_function():
    return "Hello from Cython!"

def add(int a, int b):
    return a + b

def subtract(int a, int b):
    return a - b

def multiply(int a, int b):
    return a * b

def divide(double a, double b):
    if b == 0:
        return float('inf')
    return a / b

def greet(str name):
    return f"Hello, {name}!"

def is_even(int n):
    return n % 2 == 0

def max_of_two(int a, int b):
    return a if a > b else b

def factorial(int n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(int n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def square(double x):
    return x * x

def cube(double x):
    return x * x * x

def power(double base, int exponent):
    cdef int i
    cdef double result = 1.0
    for i in range(exponent):
        result *= base
    return result

def reverse_string(str s):
    return s[::-1]

def repeat_string(str s, int times):
    return s * times
