# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.


def array_front9(nums):
    stop_loop = 4
    if len(nums) < 4:
        stop_loop = len(nums)
    for i in nums:
        stop_loop -= 1
        if stop_loop <= 0:
            return False
        if i == 9:
            return True
    return False
