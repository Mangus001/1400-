import math
nums = [48, 64, 80]
gcd_value = nums[0]
for num in nums[1:]:
    while num:
        gcd_value, num = num, gcd_value % num
print(gcd_value)
