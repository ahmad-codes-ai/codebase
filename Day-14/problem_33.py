# Problem 33
# The Multi-Agent Task Dependency Matcher
# 
# An AI agent cannot run task B until task A is completely clear. Given a list of finished tasks, check if the string "task_alpha" exists in that list; if it does, print "Proceeding to beta", else print "Dependency block active".


finished_tasks = ["task_setup", "task_alpha", "task_cleanup", "task_logging"]

for i in finished_tasks:
  if i.lower() == 'task_alpha':
    print("Proceeding to beta")
  else:
    print("Dependency block active")

