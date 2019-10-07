class Persons:
    name = None
    age = None

    def __init__(self, name, age):
        self._age = age
        self._name = name

    def setName(self, name):
        self._name = name

    def setAge(self, age):
        self._age = age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    @staticmethod
    def displayAllInfo():
        print("name:{} and age:{}".format(Persons.name,Persons.age))