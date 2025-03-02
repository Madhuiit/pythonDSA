def twoSum(nums , target):
    seen = {}
    for i ,num in enumerate(nums):
        compliment = target - num
        if compliment in seen :
            return [seen[compliment],i]
        seen[num]=i
    return []


n = [2,7,11,15]
target = 9
print(twoSum(n,target))
