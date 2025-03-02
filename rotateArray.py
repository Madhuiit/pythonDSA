def rotate(arr,k):
    n = len(arr)
    k = k%n # handle k>n
    arr[:]= arr[-k:]+ arr[:-k]
    return arr
print(rotate([8,9,7,5,3,5],3))