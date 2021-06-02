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


def first_two(text):
    try:
        return text[0] + text[1]
    except:
        return text


"""
https://codingbat.com/prob/p107010
Given a string of even length, return the first half. So the string "WooHoo"
yields "Woo".
"""


def first_half(text):
    new_text = ""
    for i in range(len(text) / 2):
        new_text += text[i]
    return new_text


"""
https://codingbat.com/prob/p138533
Given a string, return a version without the first and last char, so "Hello"
yields "ell". The string length will be at least 2.
"""


def without_end(text):
    new_text = ""
    for i in range(len(text)):
        if i == 0 or i == len(text) - 1:
            continue
        else:
            new_text += text[i]
    return new_text


"""
https://codingbat.com/prob/p194053
Given 2 strings, a and b, return a string of the form short+long+short,
with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty (length 0).
"""


def combo_string(a, b):
    if len(a) > len(b):
        long_str = a
        short_str = b
    elif len(b) > len(a):
        long_str = b
        short_str = a
    elif len(a) == len(b):
        return ""
    return short_str + long_str + short_str


"""
https://codingbat.com/prob/p127703
Given 2 strings, return their concatenation, except omit the first char of
each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""


def non_start(a, b):
    def remove_first_char(text):
        text_without_first_char = ""
        for i in range(len(text)):
            if i == 0:
                continue
            text_without_first_char += text[i]
        return text_without_first_char
    return remove_first_char(a) + remove_first_char(b)


"""
https://codingbat.com/prob/p160545
Given a string, return a "rotated left 2" version where the first 2 chars are
moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""


def left2(text):
    first_chars = ""
    last_chars = ""
    for i in range(len(text)):
        if i == 0 or i == 1:
            first_chars += text[i]
        else:
            last_chars += text[i]
        print("i:{}, first:{}, last:{}".format(
            i, first_chars, last_chars))
    return last_chars + first_chars
