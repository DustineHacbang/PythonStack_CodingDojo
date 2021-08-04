class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.energy = 50

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health} \nEnergy: {self.energy}")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        
        return self

    def hook_attack (self, ninja):
        ninja.health -= self.speed*1.5
        return self
    
    def angry_attack (self, ninja): 
        ninja.health -= self.strength * 2 
        self.energy -= self.strength
        return self
    
    def drink_rum (self): 
        if self.health <= 50:
            print("Too imapaired to fight!")
        else:
            self.strength *= 4 
            self.health -= 50 
        return self
