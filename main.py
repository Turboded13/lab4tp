"""
@file main.py
@brief A simple script to check if a given string is a palindrome
"""

def is_palindrome(s: str) -> bool:
    """
    @brief Check if the given string is a palindrome.
    @param s The string to be checked.
    @return True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_string = "A man, a plan, a canal, Panama"
    result = is_palindrome(test_string)
    print(f"The string '{test_string}' is a palindrome: {result}")