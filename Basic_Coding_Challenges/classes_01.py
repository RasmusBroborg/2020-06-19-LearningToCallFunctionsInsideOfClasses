# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

def video_one():
    class Employee:
        def __init__(self, firstname, lastname, pay):
            self.firstname = firstname
            self.lastname = lastname
            self.pay = pay
            email = self.email = (firstname.lower()) + \
                '.' + lastname.lower() + '@gmail.com'

        def fullname(self):
            return '{} {}'.format(self.firstname, self.lastname)

    emp_1 = Employee('John', 'Smith', '30000')
    emp_2 = Employee('Testing', 'User', '2000')

    print(Employee.fullname(emp_1))
    print(emp_1.email)

# Test video 1 below:
# video_one()


# https://www.youtube.com/watch?v=BJ-VvGyQxho
