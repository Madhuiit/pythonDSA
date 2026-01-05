# find top 3 most frequent element in a list

from collections import Counter
nums  = [1,2,2,3,3,3,4,4,4,4,5]

print(Counter(nums).most_common(3))