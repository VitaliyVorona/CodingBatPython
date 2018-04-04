# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


def array123(nums):
    array_pattern = [1, 2, 3]
    for index in range(len(nums) - 2):
        if nums[index: index + 3] == array_pattern:
            return True
    return False
