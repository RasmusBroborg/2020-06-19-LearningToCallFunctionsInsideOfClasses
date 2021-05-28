"""
https://codingbat.com/prob/p193507
Given a string and a non-negative int n, return a larger string that is n
copies of the original string.
"""


def string_times(the_string, n):
    return the_string * n


"""
https://codingbat.com/prob/p165097
Given a string and a non-negative int n, we'll say that the front of the
string is the first 3 chars, or whatever is there if the string is less
than length 3. Return n copies of the front;
"""


def front_times(the_string, n):
    if len(the_string) <= 3:
        return the_string * n
    else:
        return (the_string[0] + the_string[1] + the_string[2]) * n


"""
https://codingbat.com/prob/p113152
Given a string, return a new string made of every other char starting with
the first, so "Hello" yields "Hlo".
"""


def string_bits(the_string):
    new_string = ""
    include = True
    for i in range(len(the_string)):
        if include == True:
            new_string += the_string[i]
            include = False
        elif include == False:
            include = True
    return new_string


"""
https://codingbat.com/prob/p118366
Given a non-empty string like "Code" return a string like "CCoCodCode".
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""


def string_splosion(the_string):
    len_string = len(the_string)
    new_string = ""
    iterator = 1
    while iterator <= len_string:
        for i in range(iterator):
            new_string += the_string[i]
        iterator += 1
    return new_string


"""
https://codingbat.com/prob/p145834
Given a string, return the count of the number of times that a substring
length 2 appears in the string and also as the last 2 chars of the string,
so "hixxxhi" yields 1 (we won't count the end substring).

# print(last2('hixxhi'))  # → 1
# print(last2('xaxxaxaxx'))  # → 1
# print(last2('axxxaaxx'))  # → 2
"""


def last2(the_string):
    string_len = len(the_string)
    count = 0
    if string_len >= 4:
        substring = the_string[string_len - 2] + \
            the_string[string_len - 1]
    else:
        return 0
    # -2 to ignore the last two chars in the string, -1 to compensate
    # as the code below checks both the current index value AND upcoming index value
    for i in range(string_len - 2 - 1):
        ref_substring = the_string[i] + the_string[i + 1]
        if ref_substring == substring:
            count += 1
    return count


"""
https://codingbat.com/prob/p166170
Given an array of ints, return the number of 9's in the array.
array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""


def array_count9(nums):
    iterator = 0
    for element in nums:
        if element == 9:
            iterator += 1
    return iterator


"""
https://codingbat.com/prob/p110166
Given an array of ints, return True if one of the first 4 elements in the array
is a 9. The array length may be less than 4.
"""


def array_front9(nums):
    iterator = 0
    for element in nums:
        iterator += 1
        if iterator > 4:
            return False
        if element == 9:
            return True
    return False


"""
https://codingbat.com/prob/p193604
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears
in the array somewhere.
"""


def array123(nums):
    for i in range(len(nums)):
        try:
            if (nums[i], nums[i + 1], nums[i + 2]) == (1, 2, 3):
                return True
        except:
            break
    return False
