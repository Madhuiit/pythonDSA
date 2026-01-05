# def maxSubArraySum(arr):
#         max = 0
#         l = set()
#         for i in range(0,len(arr)):
#             s = set()
#             sum =0
#             for j in range(i,len(arr)):
#                 sum+=arr[j]
#                 s.add(arr[j])
#                 if sum>=max:
#                     max = sum
#                     l = s
#         return l

# print(maxSubArraySum([1 ,2, 3 ,-2 ,5]))

def countLessEq(self,a,b):
    def binary_search(arr,x):
        low , high = 0,len(arr)-1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] <= x:
                ans =mid
                low = mid+1
            else:
                high = mid -1
        return ans +1
    
    b.sort()
    result = []
    for val in a:
        count = binary_search(b,val)
        result.append(count)
    return result

