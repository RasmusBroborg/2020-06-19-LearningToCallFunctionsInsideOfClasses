"""
https://codingbat.com/prob/p181624
Given an array of ints, return True if 6 appears as either the first or last
element in the array. The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""


def first_last6(nums):
    if nums[0] == 6 or nums[len(nums) - 1] == 6:
        return True
    else:
        return False


"""
https://codingbat.com/prob/p179078
Given an array of ints, return True if the array is length 1 or more, and the
first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""


def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False


"""
https://codingbat.com/prob/p113659
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
"""


def make_pi():
    # How is this considered a challenge? Am I missing something obvious?
    return [3, 1, 4]


"""
https://codingbat.com/prob/p147755
Given 2 arrays of ints, a and b, return True if they have the same first
element or they have the same last element. Both arrays will be length 1 or more.

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""


def common_end(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False


"""
https://codingbat.com/prob/p191645
Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""


def sum3(nums):
    return sum(nums)


"""
https://codingbat.com/prob/p148661
Given an array of ints length 3, return an array with the elements "rotated
left" so {1, 2, 3} yields {2, 3, 1}.
"""


def rotate_left3(nums):
    nums.append(nums[0])
    nums.pop(0)
    return nums


"""
https://codingbat.com/prob/p192962
Given an array of ints length 3, return a new array with the elements in
reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""


def reverse3(nums):
    reversed_nums = []
    for i in range(len(nums)):
        reversed_nums.insert(0, nums[i])
    return reversed_nums


"""
https://codingbat.com/prob/p135290
Given an array of ints length 3, figure out which is larger, the first or last
element in the array, and set all the other elements to be that value. Return
the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""


def max_end3(nums):
    upd_nums = []
    if nums[0] > nums[-1]:
        highest_num = nums[0]
    else:
        highest_num = nums[-1]
    for i in range(len(nums)):
        upd_nums.append(highest_num)

    return upd_nums


"""
https://codingbat.com/prob/p192589
Given an array of ints, return the sum of the first 2 elements in the array.
If the array length is less than 2, just sum up the elements that exist,
returning 0 if the array is length 0.

sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""


def sum2(nums):
    if len(nums) == 1:
        return nums[0]# EJ FÄRDIG
