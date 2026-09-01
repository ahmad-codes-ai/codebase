'''
Easy Problem 10 – Simple Game Character
Context A role-playing game has characters with health and attack power.

Task Create a Character class with:

Private attributes: __name, __health, __attack.
Methods: take_damage(damage) – reduces health (not below 0).
attack_enemy(enemy) – deals damage to another character.
Getters for health and attack.
Override __str__ to show name and health.
Create a Team class that:

Has a list of Character objects.
Methods: add_character(char), get_total_health() – sum of all health.
Sample Usage

hero = Character("Hero", 100, 20)
goblin = Character("Goblin", 50, 10)
hero.attack_enemy(goblin)  # goblin health becomes 30
team = Team()
team.add_character(hero)
team.add_character(goblin)
print(team.get_total_health())  # 130
'''


class Character:
  def __init__(self,name,health,attack):
    self.__name = name
    self.__health = health
    self.__attack = attack

  def take_damage(self,damage):
    if self.__health - damage > 0:
      self.__health-=damage
    else:
      self.__health = 0

  def attack_enemy(self,enemy):
    enemy.take_damage(self.__attack)

  def get_health(self):
    return self.__health

  def get_attack(self):
    return self.__attack

  def __str__(self):
    return f"Name: {self.__name}, Health: {self.__health}"


class Team:
  def __init__(self):
    self.characters = []

  def add_character(self,ch):
    if ch not in self.characters:
      self.characters.append(ch)
      return True
    return False

  def get_total_health(self):
    total = 0
    for i in self.characters:
      total+=i.get_health()
    return total

hero = Character("Hero", 100, 20)
goblin = Character("Goblin", 50, 10)
hero.attack_enemy(goblin)  # goblin health becomes 30
team = Team()
team.add_character(hero)
team.add_character(goblin)
print(team.get_total_health())  # 130    