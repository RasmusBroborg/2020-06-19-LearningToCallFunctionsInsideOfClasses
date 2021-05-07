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
