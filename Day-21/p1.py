''' Build a flashcard using class in python. A flashcard is a card having information on both sides, which can
 be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

Example 1:

Approach:

Create a class named FlashCard.

Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as
value. E.g., {"Banana": "yellow", "Strawberries": "pink"}

Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value 
in variable color.

Now prompt the user to answer the color of the randomly chosen fruit.
If correct print correct else print wrong. '''



import random

class Game:

  def __init__(self):
    self.apple = 'red'
    self.banana = 'yellow'
    self.strawberry = 'red'
    self.show()

  def show(self):
    while self.__dict__:

      chosen = random.choice(list(self.__dict__.items()))
      k,v = chosen
      us = input(f"\n Enter the color of {k}: ")

      if us == v:
        print("Correct")
      else:
        print("Incorrect")

      pl = int(input("Enter 1 to play again or 0 to quit: "))

      if pl == 0:
        print("Goodbye")
        break

      self.__dict__.pop(k)

    else:
      print("Goodbye Game ended")


p1 = Game()