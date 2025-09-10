# Max product pair

def max_product(nums):
    max_p = nums[0] * nums[1]
    pair = (nums[0], nums[1])
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            p = nums[i] * nums[j]
            if p > max_p:
                max_p = p
                pair = (nums[i], nums[j])
    return pair, max_p

nums = [3,5,-2,9,-10]
res = max_product(nums)

print("Product : ",res)