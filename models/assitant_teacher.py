from models.employer import Employer
from models.students import Students

# Demo multi inheritance python
class AssitantTeacher(Employer, Students):
    
    def __init__(self, name, age, salary, school_name):
        Employer().__init__(name, age, salary)
        Students().__init__(school_name)
