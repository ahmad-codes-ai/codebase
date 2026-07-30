'''
Easy Problem 5 – To-Do List with Priorities
Context A simple task manager where tasks have a priority (1 = high, 2 = medium, 3 = low).

Task Create a Task class with:

Private attributes: __title, __priority, __completed (bool).
Methods: mark_done(), mark_pending().
Override __lt__ so that tasks with lower priority number come first.
Override __str__.
Create a TodoList class that:

Has a list of Task objects.
Methods: add_task(task), get_tasks_sorted() – returns sorted list (using __lt__).
get_completed_tasks() and get_pending_tasks().
Sample Usage

todo = TodoList()
todo.add_task(Task("Write report", 2))
todo.add_task(Task("Fix bug", 1))   # high priority
todo.add_task(Task("Clean desk", 3))
sorted_tasks = todo.get_tasks_sorted()
print([t.title for t in sorted_tasks])  # Fix bug, Write report, Clean desk
'''


class Task:
  def __init__(self,title,pri,comp=False):
    self.__title = title
    self.__priority = pri 
    self.__completed = comp

  def mark_done(self):
    self.__completed = True
  
  def mark_pending(self):
    self.__completed = False

  def get_status(self):
    if self.__completed:
      return True
    return False

  def get_title(self):
    return self.__title

  def __str__(self):
    return f"{self.__title} (Priority: {self.__priority}) - {'Done' if self.__completed else 'Pending'}"

  def __lt__(self,other):
    return self.__priority < other.__priority


class TodoList:
  def __init__(self):
    self.tasks = []

  def add_task(self,task):
    if task not in self.tasks:
      self.tasks.append(task)
      return True
    return False

  def get_tasks_sorted(self):
    return sorted(self.tasks)

  def get_completed_tasks(self):
    t = []
    for i in self.tasks:
      if i.get_status():
        t.append(i)
    return t

  def get_pending_tasks(self):
    t = []
    for i in self.tasks:
      if not i.get_status():
        t.append(i)
    return t

todo = TodoList()
todo.add_task(Task("Write report", 2))
todo.add_task(Task("Fix bug", 1))   # high priority
todo.add_task(Task("Clean desk", 3))
sorted_tasks = todo.get_tasks_sorted()
print([t.get_title() for t in sorted_tasks])  # Fix bug, Write report, Clean desk