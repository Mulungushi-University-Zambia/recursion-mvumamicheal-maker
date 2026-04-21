def check_palindrome(word):
    # Convert word to lowercase to ensure case-insensitivity
    word = word.lower()
    
    # Convert string into an array (list) of characters
    char_array = list(word)
    
    # Create the reversed array
    # The [::-1] syntax is the standard way to reverse a list in Python
    reversed_array = char_array[::-1]
    
    # Compare the two arrays
    if char_array == reversed_array:
        return True
    else:
        return False

def main():
    user_input = input("Enter a word to check if it is a palindrome: ")
    
    if check_palindrome(user_input):
        print(f"'{user_input}' is a Palindrome!")
    else:
        print(f"'{user_input}' is a Normal word.")

if __name__ == "__main__":
    main()