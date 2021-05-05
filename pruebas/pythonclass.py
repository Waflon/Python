

class User:
    def __init__(self,name,adress):
        self.name=name
        self.address = adress
    
    def displayName(self):
        print(self.name)

    def setName(self,name):
        self.name =name