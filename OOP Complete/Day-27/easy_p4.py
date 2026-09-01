'''
Problem 4: Simple Agent - Data Collector
Scenario: You are building a simple data collection agent.

Task:

Create a base class Agent with attributes name, and status (e.g., "idle" or "active").

Create a method start() that sets status to "active" and prints a message.

Create a method stop() that sets status to "idle" and prints a message.

Create a subclass DataCollectorAgent.

The DataCollectorAgent should have an additional attribute data_source (e.g., "API", "Database").

Add a method collect_data() that prints a message indicating it's collecting from its data_source.
'''


class Agent:
  def __init__(self,name):
    self.name = name
    self.status = 'idle'

  def start(self):
    self.status = 'active'
    print(f"{self.name} is active")

  def stop(self):
    self.status = 'idle'
    print(f"{self.name} is now idle")

class DataCollectorAgent(Agent):
  def __init__(self,name,source):
    super().__init__(name)
    self.data_source = source

  def collect_data(self):
    if self.status == 'active':
      print(f"Agent {self.name} is active and collecting data form: {self.data_source}")
      return True
    else:
      print(f"Agent {self.name} is idle not doing anything")
      return False

web_scraper = DataCollectorAgent('scraper','wikipedia.com')
web_scraper.start()
web_scraper.collect_data()