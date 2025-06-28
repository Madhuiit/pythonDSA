def getSecondLargest(arr):
        if len(arr)<2:
            return -1
        uniqueElement = list(sorted(set(arr),reverse=True))
        
        if len(uniqueElement)<2:
            return -1
        else:
            return uniqueElement[1]
        
print(getSecondLargest([1,1, 2, 3, 4, 5]))  # Output: 4