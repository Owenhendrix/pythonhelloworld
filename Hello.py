import sys

def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(__name__)
if __name__ == "__main__":
    print(sys.orig_argv[2])
    num  = int(sys.orig_argv[2])
    print(f"Yo answer is: {factorial_iterative(num)}")

