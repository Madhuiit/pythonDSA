def removeDuplicate(arr):
    if not arr :
        return 0
    write_idx = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[write_idx]=arr[i]
            write_idx +=1
    return write_idx
print(removeDuplicate([1,1,2,3,3]))