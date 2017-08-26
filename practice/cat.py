from pet import pet;
class cat(pet):

    def __init__(self,name,heats_dogs):
        pet.__init__(self,name,"cat")
        self.hates_dogs=heats_dogs

    def hatesDog(self):
        return self.hates_dogs
    
        
