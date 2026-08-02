'''
Medium Problem 3 – Online Quiz Platform with Leaderboards
Context A quiz platform hosts multiple quizzes. Users can take quizzes, and their scores are recorded. The system computes rankings and awards badges based on performance.

Task Create the following classes:

Question

Attributes: text, options (list), correct_index.
Method: is_correct(answer_index).
Quiz

Attributes: title, questions (list).
Methods: add_question(q), get_total_questions().
Override __len__ to return number of questions.
User

Private: __username, __scores (dict: quiz_title -> score).
Methods: take_quiz(quiz, answers) – stores score (percentage).
get_average_score() – average of all taken quizzes.
Leaderboard (static class)

Class method: get_rankings(users, quiz_title) – returns list of (username, score) sorted descending.
Static method: top_performers(users, threshold=80) – returns users with average > threshold.
Badge (abstract)

Attributes: name, icon.
Abstract method: is_earned(user).
PerfectScoreBadge (inherits Badge) – earned if user has any 100% score.

MarathonBadge (inherits Badge) – earned if user took > 5 quizzes.

Sample Usage

q1 = Question("2+2?", ["3","4","5"], 1)
quiz = Quiz("Math 101")
quiz.add_question(q1)
user = User("Alice")
user.take_quiz(quiz, [1])  # correct
print(user.get_average_score())  # 100.0
badge = PerfectScoreBadge("Perfect", "⭐")
print(badge.is_earned(user))  # True
'''


from abc import ABC, abstractmethod

class Question:
  def __init__(self,text,option,correct):
    self.text = text
    self.options = option
    self.correct_index = correct 

  def is_correct(self,answer_index):
    if self.correct_index == answer_index:
      return True
    return False

class Quiz:
  def __init__(self,title):
    self.title = title
    self.questions = []

  def add_question(self,q):
    if q not in self.questions:
      self.questions.append(q)
      return True
    return False

  def get_total_questions(self):
    total = 0
    for i in self.questions:
      total+=1
    return total

  def __len__(self):
    ans = self.get_total_questions()
    return ans

class User:
  def __init__(self,name):
    self.__username = name
    self.__scores = {}
    self.__attempts = 0 

  def get_scores(self):
    return self.__scores

  def get_attempts(self):
    return self.__attempts

  def get_name(self):
    return self.__username
  
  def take_quiz(self, quiz, answers):
    idx = 0
    total = len(quiz)
    correct = 0
    for i in quiz.questions:
      if i.is_correct(answers[idx]):
        correct+=1
      idx+=1
    avg = (correct / total) * 100
    self.__scores[quiz.title] = avg
    self.__attempts += 1 

  def get_average_score(self):
    s = 0
    total = 0
    for k,v in self.__scores.items():
      s+=v
      total+=1
    max_marks = total * 100
    avg = (s/max_marks)*100

    return avg
  
class Leaderboard:

  @staticmethod
  def get_rankings(users, quiz_title):
    rankings = []
    for user in users:
        score = user.get_scores().get(quiz_title)  # Returns None if quiz not found
        if score is not None:  # Only add if they actually took this quiz
            rankings.append([user.get_name(), score])
    return rankings
  
  @staticmethod
  def top_performers(users, threshold=80):
    qualified = []
    for i in users:                          # top_users = Leaderboard.top_performers([john, jane, marathon], 80)
      if i.get_average_score() > threshold:
        qualified.append(i)
    return qualified
      
class Badge(ABC):
  def __init__(self,name,icon):
    self.name = name
    self.icon = icon

  @abstractmethod
  def is_earned(self,user):
    pass

class PerfectScoreBadge(Badge):
  def is_earned(self, user):
    for i in user.get_scores().values():
      if i == 100.0:
        return True
    return False

class MarathonBadge(Badge):
  def is_earned(self, user):
    if user.get_attempts() > 5:
        return True
    return False

