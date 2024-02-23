class Ninja:
    def __init__( self,first_name , last_name , treats , pet_food , pet ):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
    # implement the following methods:
    def walk(self):
        self.pet.play()
        return self
    
         
    def feed(self):
        self.pet.eat()
        return self
         
    def bathe(self):
        self.pet.noise()
        return self
         
        


class Pet:
    def __init__( self,name , type , tricks , health , energy ):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    
    
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
    def play(self):
        self.health+=5
        return self
    def noise(self):
        print("meow") 
        return self   

pet1=Pet("micha","cat","jump",100,100)
ninja1=Ninja("klay","ayedi","chocklat","chicken",pet1)
ninja1.walk().feed().bathe()
print(pet1.energy)
print(pet1.health)