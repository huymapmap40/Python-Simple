from models.students import Students
from models.persons import Persons
from models.assitant_teacher import AssitantTeacher

class MainClass:

    def PracticePython(self):
        print("Call static method before declare instance")
        Persons.displayAllInfo()

        student1 = Students("Huy", 1000, "Life")
        person1 = Persons("Quoc", 2000)

        dict_student = {"name": student1.getName(),
                        "age": student1.getAge(),
                        "school name": student1.getSchoolName()}

        print("Student ========>", dict_student)
        print("Person ========>", {"name":person1.getName(), "age": person1.getAge()})
        student1._age = 100 # Access to protected variable

        print("New student age(method getAge) = {}".format(student1.getAge()))
        print("New student age(protected variable) = {}".format(student1._age))

        Persons.name = student1.getName()
        Persons.age = person1.getAge()
        print("Call static method after declare instance")
        Persons.displayAllInfo()

        # assitant_obj = AssitantTeacher("Huy", 25, 800, "Hardvert")
        # name = assitant_obj.getName()
        # age = assitant_obj.getAge()
        # salary = assitant_obj.getSalary()
        # school = assitant_obj.getSchoolName()
        # print("INFO ====> {} - {} - {} - {}".format(name, age, salary, school))

# Run
obj_main = MainClass()
obj_main.PracticePython()
print("Destructor MainClass instance")
del obj_main