def maximumArrayNum(arr):
    maxVal = arr[0]
    for i in arr :
        if i > maxVal:
            maxVal = i
    return maxVal
print(maximumArrayNum([3,4,5,8,11]))