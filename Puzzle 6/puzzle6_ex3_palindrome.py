# Programming for the Puzzled -- Puzzle 6
# Ex_3
# Palindrome
# By Caliber_X

def palindrome(str):

    l = len(str)
    if l <= 1:
        return True
    if str[0] == str[l - 1]:
        if palindrome(str[1: l - 1]):
            return True
    else:
        return False


user_str = input("Enter String to check for Palindrome: ")
if palindrome(user_str):
    print("Palindrome")
else:
    print("Not Palindrome")