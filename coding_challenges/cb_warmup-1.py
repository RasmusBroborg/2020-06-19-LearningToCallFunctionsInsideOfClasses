"""
https://codingbat.com/prob/p173401
The parameter weekday is True if it is a weekday, and the parameter
vacation is True if we are on vacation. We sleep in if it is not a
weekday or we're on vacation. Return True if we sleep in.

"""


def sleep_in(weekday, vacation):
    if vacation == True or weekday == False:
        return True
    else:
        return False


"""
https://codingbat.com/prob/p120546
We have two monkeys, a and b, and the parameters a_smile and b_smile
indicate if each is smiling. We are in trouble if they are both smiling
or if neither of them is smiling. Return True if we are in trouble.
"""


def monkey_trouble(a_smile, b_smile):
    if (a_smile == True and b_smile == True) or (a_smile == False and b_smile == False):
        return True
    else:
        return False


"""
https://codingbat.com/prob/p141905
Given two int values, return their sum. Unless the two values are the same,
then return double their sum.
"""


def sum_double(a, b):
    # if the same double
    if a == b:
        return (a + b) * 2
    else:
        return a + b


"""
https://codingbat.com/prob/p197466
Given an int n, return the absolute difference between n and 21, except
return double the absolute difference if n is over 21.
"""


def diff21(n):
    if n > 21:
        difference = (n - 21) * 2
    elif n == 21:
        difference = 0
    elif n < 21 and n >= 0:
        difference = 21 - n
    elif n < 0:
        difference = (n * -1) + 21
    return difference


"""
https://codingbat.com/prob/p166884
We have a loud talking parrot. The "hour" parameter is the current hour
time in the range 0..23. We are in trouble if the parrot is talking and
the hour is before 7 or after 20. Return True if we are in trouble.
"""


def parrot_trouble(talking, hour):
    if talking == True:
        if hour < 7 or hour > 20:
            return True
        else:
            return False
    else:
        return False


"""
https://codingbat.com/prob/p124984
Given 2 ints, a and b, return True if one if them is 10 or if their sum
is 10.
"""


def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


"""
https://codingbat.com/prob/p124676
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
computes the absolute value of a number.
"""


def near_hundred(n):
    if n > 0:
        n_absolute = abs(n)
        if (n_absolute >= 90 and n_absolute <= 110) or (n_absolute >= 190 and n_absolute <= 210):
            return True
        else:
            return False
    else:
        return False


"""
https://codingbat.com/prob/p162058
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both
are negative.
"""


def pos_neg(a, b, negative):
    if negative == False:
        if (a < 0 and b >= 0) or (b < 0 and a >= 0):
            return True
        else:
            return False
    elif negative == True:
        if a < 0 and b < 0:
            return True
        return False
    else:
        return False


"""
https://codingbat.com/prob/p189441
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
"""


def not_string(a_string):
    if len(a_string) >= 3:
        if a_string[0] == "n" and a_string[1] == "o" and a_string[2] == "t":
            return a_string

    new_strng = "not " + a_string
    return new_strng


"""
https://codingbat.com/prob/p149524
Given a non-empty string and an int n, return a new string where the char
at index n has been removed. The value of n will be a valid index of a char
in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
"""


def missing_char(stri, n):
    new_string = ""
    for i in range(len(stri)):
        if i != n:
            new_string += stri[i]
    return new_string


"""
https://codingbat.com/prob/p153599
Given a string, return a new string where the first and last chars have
been exchanged.
"""


def front_back(stri):
    string_len = len(stri)
    string_first_letter = stri[0]
    string_last_letter = stri[string_len - 1]
    new_string = ""

    for i in range(string_len):
        if i == 0:
            new_string += string_last_letter
        elif i == (string_len - 1):
            new_string += string_first_letter
        else:
            new_string += stri[i]

    return new_string


"""
https://codingbat.com/prob/p147920
Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there. Return
a new string which is 3 copies of the front.
"""


def front3(string_a):
    if len(string_a) <= 3:
        return string_a * 3
    else:
        return (string_a[0] + string_a[1] + string_a[2]) * 3
