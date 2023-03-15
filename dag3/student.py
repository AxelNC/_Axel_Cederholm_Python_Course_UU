class Student(Person):
    def __init__(self, name, surname, subjct):
        super().__init__(name,surname)
        self.subject = subject
        
    def getSubject(self):
        return self.subject 