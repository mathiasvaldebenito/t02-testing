class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

class Seperhero(Person):
    def __init__(self):
        super().__init__()
    
    def rescue(self,cat):
        if cat.in_tree :
            cat.in_tree == False

        
