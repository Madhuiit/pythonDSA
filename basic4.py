def subarraySum(arr, target):
        for i in range(len(arr)):
            sum=0
            for j in range(i,len(arr)):
                
                sum+=arr[j]
                if sum ==target:
                    return [i,j]
        return -1



arr = [26, 3 ,28, 7]

target = 52
print(subarraySum(arr,target))