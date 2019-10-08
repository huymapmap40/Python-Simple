from models.persons import Persons

class Employer(Persons):
    
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary
    
    def setSalary(self, salary):
        self._salary = salary

    def getSalary(self):
        return self._salary