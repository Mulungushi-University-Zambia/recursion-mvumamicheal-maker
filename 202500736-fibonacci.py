def fibonacci(n):
    """Recursive function to calculate nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    try:
        num = int(input("Enter a non-negative integer for Fibonacci: "))
        if num < 0:
            print("Invalid input: Please enter a non-negative integer.")
        else:
            print(f"The Fibonacci number at position {num} is {fibonacci(num)}")
    except ValueError:
        print("Invalid input: Please enter a valid integer.")

if __name__ == "__main__":
    main()


