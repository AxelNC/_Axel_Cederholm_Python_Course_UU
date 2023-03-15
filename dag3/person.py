class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def getNames(self):
        return self.name, self.surname