nums = [1,2,3,4,5]
nums_ = [1,2,1,1,2,3,4,5]
res = []
for i in nums:
    res.append(i*i)

nums1 = [x*x for x in nums]

even = [x for x in nums if x%2 == 0]

st1 = {x for x in nums_}

print(st1)
print(even)