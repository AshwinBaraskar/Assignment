'''Write a function that checks if a given word is a palindrome. Character case should be ignored'''


def palindrome(name):
    if name.lower() == name[::-1].lower():
        print("Palindrome")
    else:
        print("Not Palindrome")


palindrome("Radar")  # palindrome
palindrome("xyz")  # Not Palindrome
