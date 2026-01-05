import string
text = "Hello ,world! Data@Science."
clean = "".join(c for c in text if c not in string.punctuation)

print(clean)