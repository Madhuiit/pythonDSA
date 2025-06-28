def maxSubArraySum(arr):
        max = 0
        l = set()
        for i in range(0,len(arr)):
            s = set()
            sum =0
            for j in range(i,len(arr)):
                sum+=arr[j]
                s.add(arr[j])
                print(s)
                if sum>=max:
                    max = sum
                    l = s
        return l

print(maxSubArraySum([1 ,2, 3 ,-2 ,5]))