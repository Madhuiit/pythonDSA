#grouph words by first letter
from collections import defaultdict
words = ["apple","ant","bananan","ball","cat","car"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)
print(dict(grouped))