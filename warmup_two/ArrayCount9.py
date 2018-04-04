# Given an array of ints, return the number of 9's in the array.


def array_count9(nums):
    count_nums = {9: 0}
    for i in nums:
        if i == 9:
            count_nums[i] += 1
    return count_nums[9]
