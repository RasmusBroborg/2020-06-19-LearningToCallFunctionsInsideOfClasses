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

# Test code by running function:
# video_one()


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

# Test code by running function:
# video_two()

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


# ------- VIDEO 4 --------
# https://www.youtube.com/watch?v=RSl87lqOXDE

def video_four():
    class Employee:

        # Class variables
        raise_amount = 1.04

        # Class init method

        def __init__(self, firstname, lastname, pay):
            self.firstname = firstname
            self.lastname = lastname
            self.email = firstname + \
                '.' + lastname + '@gmail.com'
            self.pay = pay

        # methods
        def fullname(self):
            return '{} {}'.format(self.firstname, self.lastname)

        def apply_raise(self):
            self.pay = int(float(self.pay) * self.raise_amount)

    class Developer(Employee):
        raise_amount = 1.02

        def __init__(self, firstname, lastname, pay, prog_lang):
            super().__init__(firstname, lastname, pay)
            self.prog_lang = prog_lang

    class Manager(Employee):

        def __init__(self, firstname, lastname, pay, employees=None):
            super().__init__(firstname, lastname, pay)
            if employees is None:
                self.employees = []
            else:
                self.employees = employees

        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)

        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

        def print_employees(self):
            for emp in self.employees:
                print('--> ' + emp.fullname())

                # Testing the class
    dev_1 = Developer('John', 'Smith', '30000', 'Python')
    dev_2 = Developer('Testing', 'User', '2000', 'Javascript')

    mgr_1 = Manager("Sue", 'Smith', 90000, [dev_1, dev_2])

    print(isinstance(mgr_1, Manager))
    print(issubclass(Manager and Developer, Employee))

    # print(mgr_1.email)
    # mgr_1.print_employees()
    # print("Will now remove one employee: ")
    # mgr_1.remove_emp(dev_2)
    # mgr_1.print_employees()


# Test code by running function:
# video_one()
# video_two()
# video_three()
video_four()
