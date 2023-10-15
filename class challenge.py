
#defining initial parent class
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printNameAge(self):
        print("{} is {} years old!".format(self.name, self.age))

#object made from the parent class
Nic = person("Nic", 21)
Nic.printNameAge()

#defining a child class called "student" from the "person" parent class,
#with additional gpa and grade attributes
class student(person):
    def __init__(self, name, age, gpa, grade):
        super().__init__(name, age)
        self.gpa = gpa
        self.grade = grade

    def printStudentStats(self):
        print("{} is a {} year old {} with a {} gpa!".format(self.name, self.age, self.grade, self.gpa))


# object made from the student child class
StudentNic = student("Nic", 21, 4.0, "Senior")
StudentNic.printStudentStats()

