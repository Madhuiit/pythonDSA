def isPalindrom(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(isPalindrom("pop"))