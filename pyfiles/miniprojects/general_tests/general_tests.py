def keyword_assert():
    """
    The assert keyword is used when debugging code.
    The assert keyword lets you test if a condition in your code returns True,
    if not, the program will raise an AssertionError.
    """

    x = 'Hello'

    # if condition returns True, nothing happens:
    assert x == 'Hello'

    # if condition returns False, AssertionError is raised:
    assert x == 'Goodbye', 'x should be "Hello"'


# assert_keyword()


def type_numeric():
    """
    There are three numeric types in Python:
    - int
    - float
    - complex

    """
    x = 1    # int
    y = 2.2e-10  # float
    z = 1j   # complex

    x = complex(x)

    print(x, y, z)
    print(type(z))
    print(type(y))


# type_numeric()

def type_collections():
    """
    There are four collection data types in the Python programming language:

    - List is a collection which is ordered and changeable. Allows duplicate members.
    - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    - Set is a collection which is unordered and unindexed. No duplicate members.
    - Dictionary is a collection which is ordered* and changeable. No duplicate members.
    """

    def my_list():
        # List items are ordered, changeable, and allow duplicate values.
        # Can contain different data types.

        list_1 = ['banana', 4, 1e2, 'banana']

        print(type(list_1[2]))
        print(type(list_1))
        print(type(list_1[1]))
        print(list_1)

        # You can also create a list using the list() constructor:
        list_2 = list(('abba', 2, 'gemini'))
        print(list_2)
        print(type(list_2))

    # my_list()

    def my_tuple():
        # A tuple is a collection which is ordered and unchangeable.
        # More memory efficient than lists == less space and a tad bit faster.
        # Written with round brackets ().

        thistuple = ('ham', 'bacon', 2)

        print(thistuple)
        try:
            thistuple[1] = 'jelly'
        except TypeError:
            print('TypeError. Next except message will not be shown.')
        except:
            print('Tuples are unchangeable.')
        finally:
            print("Cleanup, irrespective of any exceptions.")

    # my_tuple()

    def my_set():
        # Also known as
        # Set items are unordered, unchangeable, and do not allow duplicate values.
        # Sets are written with curly brackets.
        list_with_duplicates = [1, 3, 2, 3, 1, 3, 2]
        set_without_duplicates = set(list_with_duplicates)

        print(type(set_without_duplicates))
        print(set_without_duplicates)

    # my_set()


# type_collections()

def test_import_file():

    file1 = open('test_text.txt', 'r')
    lines = file1.readlines()

    print(lines)

    count = 0
    for line in lines:
        count += 1
        print('Line {}: {}'.format(count, line))


# test_import_file()


my_tuple = (1, 2)
print(my_tuple[1])

print("Hello")
