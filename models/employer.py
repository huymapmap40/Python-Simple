from models.persons import Persons

class Employer(Persons):
    
    def __init__(self, salary):
        super().__init__()
        self._salary = salary
    
    def setSalary(self, salary):
        self._salary = salary

    def getSalary(self):
        return self._salary