"""
https://codingbat.com/python/String-1
Basic python string problems -- no loops. Use + to combine strings, len(str)
is the number of chars in a String, str[i:j] extracts the substring starting
at index i and running up to but not including index j.
"""


"""
https://codingbat.com/prob/p115413
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
"""


def hello_name(name):
    return "Hello {}!".format(name)


"""
https://codingbat.com/prob/p182144
Given two strings, a and b, return the result of putting them together in the
order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
"""


def make_abba(a, b):
    return a + b + b + a


"""
https://codingbat.com/prob/p132290
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic
text. In this example, the "i" tag makes <i> and </i> which surround the word
"Yay". Given tag and word strings, create the HTML string with tags around
the word, e.g. "<i>Yay</i>".
"""


def make_tags(tag, word):
    return "<{}>{}</{}>".format(tag, word, tag)


"""
https://codingbat.com/prob/p129981
Given an "out" string length 4, such as "<<>>", and a word, return a new
string where the word is in the middle of the out string, e.g. "<<word>>".
"""


def make_out_word(out, word):
    return out[0] + out[1] + word + out[2] + out[3]


"""
https://codingbat.com/prob/p148853
Given a string, return a new string made of 3 copies of the last 2 chars of
the original string. The string length will be at least 2.
"""


def extra_end(a_string):
    return (a_string[len(a_string) - 2] + a_string[len(a_string) - 1]) * 3


"""
https://codingbat.com/prob/p184816
Given a string, return the string made of its first two chars, so the String
"Hello" yields "He". If the string is shorter than length 2, return whatever
there is, so "X" yields "X", and the empty string "" yields the empty string "".
"""
