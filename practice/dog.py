from pet import pet;
class dog(pet):

    def __init__(self,name,chases_cats):
        pet.__init__(self,name,"dog")
        self.chases_cats=chases_cats

    def chasesCats(self):
        return self.chases_cats
    
