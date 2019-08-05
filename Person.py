from enum import Enum

class TypePerson(Enum):
    student = 1
    worker = 2

class Person:
    def __init__(self,name ="ingonito", age = None , height = None ):
        self.name = name  # if name != None else "incognito"
        self.age = age
        self.height = height

    def WhoIam(self):
        print("person1.name={} is a{}".format(self.name,type(self)))

class Student(Person):
    def __init__(self,department):
        Person.__init__(self, name="new student")
        self.department = department

class Worker(Person):
    def __init__(self,salary):
        Person.__init__(self, name="new Worker")
        self.salary = salary

class AbstactPerson():
    def __init__(self, typePerson , globalname ):
        self.myPerson = Person()
        self.typePerson = typePerson
        if (typePerson == TypePerson.student ):
            self.myPerson = Student(globalname)
        else :
            self.myPerson = Worker(globalname)

    def getPerson(self):
        return self.myPerson


instanceAbs = AbstactPerson(TypePerson.student,"dav")
instanceAbs.getPerson().WhoIam()




Person1 = Person(age=22,height=1.88)

Person2 = Student("Computer Science")
Person2.WhoIam()





# function

# create MobilePhone class
# in init print("creating a phone")
# create methods: ring, powerOn,
#   powerOff
# create secret method: factoryRestart
# create 2 phones
