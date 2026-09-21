def gen_sq(nums):
    for i in nums:
        yield i*i

# nums=gen_sq([1,2,3,4])
nums = [1, 2, 3, 4]
nums = (x*x for x in nums)
# print(list(nums))
# print(nums)
for i in nums:
    print(i)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
