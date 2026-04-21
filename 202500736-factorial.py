
def factorial(n):
    """Recursive function to calculate factorial."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        num = int(input("Enter a non-negative integer for Factorial: "))
        if num < 0:
            print("Invalid input: Please enter a non-negative integer.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input: Please enter a valid integer.")

if __name__ == "__main__":
    main()

