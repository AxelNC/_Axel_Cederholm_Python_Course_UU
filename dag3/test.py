class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def getNames(self):
        return self.name, self.surname


class Student(Person):
    def __init__(self, name, surname, subject):
        super().__init__(name,surname)
        self.subject = subject
        
    def getSubject(self):
        return self.subject 


axel = Person("Axel", "Cederholm")

student = Student(axel, "medicine")


print(student.getNames)

print(student.getSubject)