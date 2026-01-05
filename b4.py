#checking palindrome
def palindrome(n:str) -> bool:
    return n == n[::-1]
print(palindrome("111"))