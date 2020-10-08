from models.persons import Persons

class Students(Persons):

    # Full constructor
    def __init__(self, name, age, school_name):
        super().__init__(name, age)
        self._school_name = school_name

    def setSchoolName(self, school_name):
        self._school_name = school_name

    def getSchoolName(self):
        return self._school_name