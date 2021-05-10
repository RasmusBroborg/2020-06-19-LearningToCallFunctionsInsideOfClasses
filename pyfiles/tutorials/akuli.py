# https://github.com/Akuli/python-tutorial

import datetime

# --- Defining and using custom classes ---
# https://github.com/Akuli/python-tutorial/blob/master/basics/classes.md


def print_reset():
    print("""    --------------------------------
    RESET {}
    --------------------------------""".format(datetime.datetime.now()))


def basics_classes():
    class Website:
        def __init__(self):
            self.url = 'URL missing'
            self.founding_year = 'founding_year missing'
            self.other = 'other missing'

    # print(Website)  # == <class '__main__.Website'>

    print_reset()

    github = Website

    github.url = 'https://github.com/'
    github.founding_year = 2008
    github.free_to_use = True

    # print(github())
    print(github.url)
    # rint(github.__dict__)
    print(Website().__dict__)


# Test chapter:
basics_classes()
