'''
Easy Problem 7 – Savings Goal Tracker
Context A person sets financial savings goals and tracks progress.

Task Create a SavingsGoal class with:

Attributes: name, target_amount, current_amount (private, initial 0).
Methods: add_savings(amount) – increases current, get_progress() – returns percentage (current/target * 100).
Class variable: total_goals – increments when a goal is created.
Class method: get_total_goals().
Create a GoalTracker class that:

Has a list of SavingsGoal objects.
Methods: add_goal(goal), get_overall_progress() – average of all goals' progress.
Sample Usage

tracker = GoalTracker()
goal1 = SavingsGoal("Vacation", 1000)
goal1.add_savings(200)
tracker.add_goal(goal1)
goal2 = SavingsGoal("New Laptop", 800)
goal2.add_savings(400)
tracker.add_goal(goal2)
print(tracker.get_overall_progress())  # (20% + 50%)/2 = 35%
print(SavingsGoal.get_total_goals())   # 2
'''

class SavingsGoal:

  total_goals = 0
  
  @staticmethod
  def get_total_goals():
    return SavingsGoal.total_goals

  def __init__(self,name,tar,crr=0):
    self.name = name
    self.target = tar
    self.current = crr
    SavingsGoal.total_goals+=1

  def add_savings(self,amount):
    self.current+=amount

  def get_progress(self):
    return (self.current/self.target) * 100

class GoalTracker:
  def __init__(self):
    self.goals = []

  def add_goal(self,goal):
    if goal not in self.goals:
      self.goals.append(goal)
      return True
    return False

  def get_overall_progress(self):
    s = 0
    for i in self.goals:
      s+=i.get_progress()
    avg = s / len(self.goals)
    return f"{avg}%"


tracker = GoalTracker()
goal1 = SavingsGoal("Vacation", 1000)
goal1.add_savings(200)
tracker.add_goal(goal1)
goal2 = SavingsGoal("New Laptop", 800)
goal2.add_savings(400)
tracker.add_goal(goal2)
print(tracker.get_overall_progress())  # (20% + 50%)/2 = 35%
print(SavingsGoal.get_total_goals())   # 2