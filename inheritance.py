class Employee:
    raise_amt = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def raise_sal(self):
        return self.pay * 1.06

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp):
        first, last, pay = emp.split('-')
        return cls(first, last, pay)

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
            super().__init__(first, last, pay)
            if employees is None:
                self.employees = []
            else:
                self.employees = employees

Emp1 = Employee('Rishabh', 'Singh', 10000)
emp = 'Rishabh-Singh-10000'
new_emp = Employee.from_string(emp)

dev1 = Developer('Rishi', 'Sunak', 30000, 'C++, Python')
Mang1 = Manager('Headshot', 'Singh', 342443,['Suresh', 'Ramesh'])
print(Mang1.employees)
print(dev1.prog_lang)


