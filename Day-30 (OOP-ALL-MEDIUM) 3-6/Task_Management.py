'''
Medium Problem 5 – Task Management with Priorities and Deadlines
Context A project management tool allows users to create tasks, assign priorities (High, Medium, Low), set deadlines, and mark completion. The system should also generate reports and sort tasks by urgency.

Task Create the following classes:

Task

Private: __title, __description, __deadline (string), __priority (int: 1=High, 2=Medium, 3=Low).
__completed (bool).
Methods: mark_done(), mark_pending().
Override __lt__ to compare by priority (lower number = higher priority).
Override __str__.
Project

Attributes: name, tasks (list).
Methods: add_task(task), remove_task(title), get_tasks_by_priority(priority).
overdue_tasks(current_date) – returns tasks with deadline < current_date and not completed.
sort_tasks() – sorts tasks in‑place using __lt__.
ReportGenerator (static class)

Static method: generate_summary(project) – returns dict with total, completed, pending, overdue counts.
Static method: export_to_string(project) – returns formatted string.
Additional

Use a class variable TASK_COUNT to auto‑increment task IDs.
Include a private __task_id.
Sample Usage

project = Project("Sprint 1")
t1 = Task("Login", "Implement login", "2026-08-01", 1)
t2 = Task("Docs", "Write docs", "2026-08-10", 3)
project.add_task(t1); project.add_task(t2)
project.sort_tasks()
report = ReportGenerator.generate_summary(project)
print(report)
'''



class Task():
  def __init__(self,title,dis,deadline,priority,completed=False):
    self.__title = title
    self.__discription = dis
    self.__deadline = deadline
    self.__priority = priority
    self.__completed = completed

  def mark_done(self):
    if not self.__completed:
      self.__completed = True
      return True
    return False

  def get_deadline(self):
    return self.__deadline

  def get_status(self):
    return self.__completed

  def get_title(self):
    return self.__title

  def mark_pending(self):
    if self.__completed:
      self.__completed = False
      return True
    return False

  def get_priority(self):
    return self.__priority

  def is_overdue(self,date):
    if date > self.__deadline:
      return True
    return False

  def __lt__(self,other):
    return self.__priority < other.__priority

  def __str__(self):
    return f"Title: {self.__title} \n Deadline: {self.__deadline} \n Priority: {self.__priority}"

class Project():

  TASK_COUNT = 0

  def __init__(self,name):
    self.name = name
    self.tasks = []

  def add_task(self,task):
    if task not in self.tasks:
      self.tasks.append(task)
      Project.TASK_COUNT+=1
      return True
    return False

  def remove_task(self,title):
    for task in self.tasks:
      if task.get_title() == title:
        self.tasks.remove(task)
        return True
    return False

  def get_tasks_by_priority(self,priority):
     return [task for task in self.tasks if task.get_priority() == priority]

  def overdue_tasks(self,current_date):
    result = []
    for task in self.tasks:
      if task.get_deadline() < current_date and not task.get_status():
        result.append(task)
    return result

  def sort_tasks(self):
    self.tasks.sort()


class ReportGenerator():

  @staticmethod
  def generate_summary(project, current_date):
    d = {
        'Total':0,
        'Completed':0,
        'Pending':0,
        'Overdue':0
    }
    for task in project.tasks:
      d['Total']+=1
      if task.get_status():
        d['Completed']+=1
      elif task.is_overdue(current_date):
        d['Overdue']+=1
      else:
        d['Pending']+=1
    return d

  @staticmethod
  def export_to_string(project,current_date):
    print(f"---- Project: {project.name} ----")
    idx = 0
    for task in project.tasks:
      idx+=1
      if task.is_overdue(current_date):
        print(f"{idx}. {task.get_title()}({task.get_priority()},{task.get_deadline()},Overdue)")
      else:
        if task.get_status():
          print(f"{idx}. {task.get_title()}({task.get_priority()},{task.get_deadline()},Completed)")
        else:
          print(f"{idx}. {task.get_title()}({task.get_priority()},{task.get_deadline()},Pending)")


# date simulated with numbers for ease