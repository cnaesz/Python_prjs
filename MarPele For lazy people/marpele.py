import random
import time
from colorama import Fore,Style
def mar():
  a_list = []
  b_list = []
  marz={}
  pelez={}
  a = random.randint(10, 100)

  for n in range(a):
      a_list.append(random.randint(1, 500))
      b_list.append(random.randint(1, 500))
      
  c = dict(zip(a_list, b_list))
  for key, value in c.items():
      if key > value:
        marz = marz | {key: value}

      if key < value:
        pelez = pelez | {key: value}
        
      else:
        marz = marz | {(key + 10): value}
        
        

  return marz, pelez


def main():
  marz, pelez = mar()
  print("marz:", marz)
  print("pelez:", pelez)



    
class Marpele_auto:
  def __init__(self):
    self.marz, self.pelez = mar()
    self.total = 0
    self.steps = 0

  def roll_dice(self):
    self.setps = 0
    """Simulate rolling a die and return the result."""
    # Initialize total to 0 for each roll
    self.total = 0
    # Roll a die (1-6)
    a = random.randint(1, 6)
    print("You rolled a", a)
    print()
    self.total += a
    self.steps += 1

    
    return self.total


  def play(self):
    print("Marpele game started!")
    while True:
  
      self.total += self.roll_dice()
      
      for key,value in self.marz.items():
        if self.total == key:         
          self.total -= value
          print(f"Mar Nishet Zad baby! {value} ta khune bargashty Aqab :P be khune {self.total}.")

      for key,value in self.pelez.items():
        if self.total == key:
          self.total += value
          print(f"Peley inam pele! hala ke {value} ta oftadi jolo chera Sedat dar nemiad?.")


      if self.total >= 1000:
        print("You reached 100! Game over.")
        print("Current total:", self.total)
        print("Steps taken:", self.steps)
        break

      print("Current total:", self.total)
      print(f"Steps taken: {Fore.GREEN}{self.steps}{Style.RESET_ALL}")
      print("Rolling again...")

   
      
      


player = Marpele_auto()
#print(list(player.marz.items()))
#print(list(player.pelez.items()))
player.play()



