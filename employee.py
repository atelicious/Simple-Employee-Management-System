class Employee:

    def __init__(self, first, last, pay, position, department, supervisor):
        self.first = first
        self.last = last
        self. pay = pay
        self.position = position
        self.department = department
        self.supervisor = supervisor

    @property
    def email(self):
        return f'{self.first}.{self.last}.email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'