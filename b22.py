# find all the pairs in the list whose sum equals to target

nums = [1,2,3,4,5,6,7]

target = 8

pairs = [(a,b) for i ,a in enumerate(nums) for b in nums[i+1:] if a+b == target]

print(pairs)