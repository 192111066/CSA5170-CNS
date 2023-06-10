import time

class PatrolBoat:
    def _init_(self, name, commander):
        self.name = name
        self.commander = commander
        self.is_sunk = False
    
    def hit_by_torpedo(self):
        print(f"The {self.name} has been hit by a torpedo!")
        self.is_sunk = True
        
    def send_message(self, message):
        if not self.is_sunk:
            print(f"Sending message from {self.name} to Australian wireless station: {message}")
        else:
            print(f"Cannot send message from {self.name} as it has been sunk!")
        
    def _str_(self):
        return f"{self.name}, under the command of {self.commander}"
        
class Torpedo:
    def _init_(self):
        self.power = 100
    
    def fire(self, target):
        print(f"Firing torpedo at {target}")
        target.hit_by_torpedo()
        
class Destroyer:
    def _init_(self):
        self.name = "Japanese destroyer"
        
    def fire_torpedo(self, target):
        print(f"Firing torpedo from {self.name}")
        torpedo = Torpedo()
        torpedo.fire(target)

def simulate_sinking():
    
    pt_109 = PatrolBoat("PT-109", "Lieutenant John F. Kennedy")
    japanese_destroyer = Destroyer()
    
    
    japanese_destroyer.fire_torpedo(pt_109)
    
    
    pt_109.send_message("PT-109 has been sunk by a Japanese destroyer.")
    time.sleep(1)
    pt_109.send_message("Requesting immediate assistance!")
    
simulate_sinking()
