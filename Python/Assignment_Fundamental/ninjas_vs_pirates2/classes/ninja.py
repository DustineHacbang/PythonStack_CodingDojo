class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.energy = 50
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health} \nEnergy:{self.energy}")

    def attack( self , pirate ):
        pirate.health -= self.strength
        if pirate.health <= 0:
            print("Ninja Wins")
        return self

    def quick_attack(self, pirate):
        pirate.health -= self.speed
        if pirate.health <= 0:
            print("Ninja Wins")
        return self

    def energy_attack(self, pirate):
        pirate.health -= self.strength * 2
        self.energy -= self.strength
        if pirate.health <= 0:
            print("Ninja Wins")
        return self
    
    def meditate(self):
        if self.health == 100:
            print(f"Health is full")
        else:
            self.health += 25
            if self.health > 100:
                self.health = 100
        if pirate.health <= 0:
            print("Ninja Wins")
        return self

    # def ninja_wins(pirate):
    #     if pirate.health <= 0:
    #         print("Winner")