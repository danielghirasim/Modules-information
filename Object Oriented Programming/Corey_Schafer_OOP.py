import datetime

class Employee():
    employee_no = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first.lower() + self.last.lower() + '@company.com'
        self.pay = round(pay, 2)
        Employee.employee_no += 1

    # def __repr__(self):
    #     return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f'{self.fullname()} -- {self.email}'

    def __add__(self, other): # Other stands for the second instance
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def fullname(self):
        return self.first.title() + ' ' + self.last.title()

    def apply_raise(self):
        self.pay *= self.raise_amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)

    @classmethod
    def change_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if datetime.datetime.weekday(day) == 5 or datetime.datetime.weekday(day) == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print(emp.fullname(), 'added to list.')

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print(f'{emp.fullname()} removed from list.')

    def print_employees(self):
        return [print('-->', x.fullname()) for x in self.employees]



dev_1 = Developer('Daniel','Ghirasim', 50000, 'Python')
dev_2 = Developer('Corey','Schafer', 90000, 'Python, Java')
emp_1 = Employee('Daniel','Ghirasim', 50000)

# print(emp_1.__str__())
# print(emp_1.__repr__())
# manager = Manager('test','manager',12344, [dev_2])
# manager.print_employees()

# print(issubclass(Manager, Employee))

# print(1+2)
# print("a"+"b")
# print(emp_1 + dev_2)
print(len(emp_1))