# Youtube link
# https://www.youtube.com/watch?v=swU3c34d2NQ&list=PL-osiE80TeTsnP0Nl1UDY8VZAlHu1m_MQ

# Closures

"""
"In simple terms: A closure is an inner function that
remembers and has access to variables in the local scope in which
it was created even after the outer function has finished executing"
"""


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func()


outer_func('Accessing inner func.')
