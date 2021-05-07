# ------- VIDEO 1 --------

# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

def video_one():
    class Employee:
        def __init__(self, firstname, lastname, pay):
            self.firstname = firstname
            self.lastname = lastname
            self.pay = pay
            self.email = firstname + \
                '.' + lastname + '@gmail.com'

        def fullname(self):
            return '{} {}'.format(self.firstname, self.lastname)

    emp_1 = Employee('John', 'Smith', '30000')
    emp_2 = Employee('Testing', 'User', '2000')

    print(Employee.fullname(emp_1))
    print(emp_1.email)


# ------- VIDEO 2 --------
# https://www.youtube.com/watch?v=BJ-VvGyQxho

def video_two():
    class Employee:

        # Class variables
        num_of_emps = 0
        raise_amount = 1.04

        # Class init method

        def __init__(self, firstname, lastname, pay):
            self.firstname = firstname
            self.lastname = lastname
            self.pay = pay
            self.email = firstname + \
                '.' + lastname + '@gmail.com'

            Employee.num_of_emps += 1

        # Class methods
        def fullname(self):
            return '{} {}'.format(self.firstname, self.lastname)

        def apply_raise(self):
            self.pay = int(float(self.pay) * self.raise_amount)

    # Testing the class

    emp_1 = Employee('John', 'Smith', '30000')
    emp_2 = Employee('Testing', 'User', '2000')

# ------- VIDEO 3 --------
# https://www.youtube.com/watch?v=rq8cL2XMM5M


def video_three():
    class Employee:

        # Class variables
        num_of_emps = 0
        raise_amount = 1.04

        # Class init method

        def __init__(self, firstname, lastname, pay):
            self.firstname = firstname
            self.lastname = lastname
            self.pay = pay
            self.email = firstname + \
                '.' + lastname + '@gmail.com'

            Employee.num_of_emps += 1

        # methods
        def fullname(self):
            return '{} {}'.format(self.firstname, self.lastname)

        def apply_raise(self):
            self.pay = int(float(self.pay) * self.raise_amount)

        # classmethods and staticmethods

        @classmethod
        def set_raise_amount(cls, amount):
            cls.raise_amount = amount

        @classmethod
        def from_string(cls, emp_str):
            firstname, lastname, pay = emp_str.split("-")
            return cls(firstname, lastname, pay)

        @staticmethod
        def is_workday(day):
            if day.weekday() == 5 or day.weekday() == 6:
                return False
            return True

    # Testing the class
    emp_1 = Employee('John', 'Smith', '30000')
    emp_2 = Employee('Testing', 'User', '2000')

    import datetime
    my_date = datetime.datetime.now()

    print(Employee.is_workday(my_date))


# Test code by running function:
# video_one()
# video_two()
video_three()
