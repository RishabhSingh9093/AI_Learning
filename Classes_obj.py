class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def raise_sal(self):
        return self.pay * 1.05
    
Emp1 = Employee('Rishabh', 'Singh', 10000)

print(Employee.full_name(Emp1))
print(Emp1.raise_sal())
print(Emp1.email)

print(Emp1.full_name())