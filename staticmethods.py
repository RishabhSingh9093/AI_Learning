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

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday() == 6:
            return False
        return True

import datetime
date = datetime.date(2016, 7, 11)
print(Employee.is_workday(date))
    
# Emp1 = Employee('Rishabh', 'Singh', 10000)
# emp = 'Rishabh-Singh-10000'
# new_emp = Employee.from_string(emp)
# print(new_emp.first)
# Emp1.set_raise_amt(1.06)
# print(Emp1.raise_amt)


