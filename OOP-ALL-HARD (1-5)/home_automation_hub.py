'''
Hard Problem 3 – Smart Home Automation Hub
Context A smart home system controls various devices (lights, thermostats, locks). The hub can schedule actions, log events, and handle voice commands.

Task Create the following classes:

Device (abstract)
Attributes: device_id, name, status (on/off), location.
Abstract methods:
turn_on()
turn_off()
get_status()
Concrete method: toggle().
Light (inherits Device)
Adds: brightness (0-100), color (tuple).
Override: turn_on() to set brightness to previous level.
Thermostat (inherits Device)
Adds: temperature, mode (cool/heat/off).
Override: turn_on() to set mode to previous.
SmartLock (inherits Device)
Adds: is_locked (bool).
Methods:
lock()
unlock() (use turn_on/off to lock/unlock).
Event (for scheduling)
Attributes: device, action (string), time (datetime).
Method: execute() – calls the appropriate action (e.g., turn_on).
Hub
Private: __devices (dict id -> device), __events (list of Event).
Methods:
register_device(device).
get_device(device_id).
schedule_event(device_id, action, time) – adds event.
run_scheduled_events() – executes all events whose time has passed and removes them.
voice_command(command) – parse string like "turn on living room light" and execute.
log_action(device, action) – records to a log (list of strings).
get_log() – returns log.
Additional Requirements

Use @abstractmethod.
Override __str__ for each device.
Use a class variable INSTANCE_COUNT to generate unique device IDs.
Use __add__ magic method on Hub to merge two hubs (combine devices and events).
Use static method to validate device types.
'''


from abc import ABC, abstractmethod

class Device(ABC):
  def __init__(self,id,name,location,status=False):
    self.id = id
    self.name = name
    self.location = location
    self.status = status

  @abstractmethod
  def turn_on(self):
    pass

  @abstractmethod
  def turn_off(self):
    pass

  @abstractmethod
  def get_status(self):
    pass

  def toggle(self):
    if self.status:
      self.turn_off()
    else:
      self.turn_on()


class Light(Device):
  def __init__(self,id,name,location,brightness,color,status=False):
    super().__init__(id,name,location,status)
    self.brightness = brightness
    self.color = color

  def set_brightness(self,level):
    if level > 0 and level <= 100:
      self.brightness = level
      return True
    return False

  def turn_on(self):
    self.status = True

  def turn_off(self):
    self.status = False

  def get_status(self):
    return self.status



class Thermostat(Device):
  def __init__(self,id,name,location,temperature,mode,status=False):
    super().__init__(id,name,location,status)
    self.temperature = temperature
    self.mode = mode

  def turn_on(self):
    self.status = True

  def turn_off(self):
    self.status = False

  def get_status(self):
    return self.status

  def change_mode(self,mode):
    if mode.lower() in ['cool','heat']:
      self.mode = mode
      return True
    return False


class SmartLock(Device):
  def __init__(self,id,name,location,status=True):
    super().__init__(id,name,location)
    self.is_locked = True

  def turn_on(self):
    self.is_locked = True
    self.status = True

  def turn_off(self):
    self.is_locked = False
    self.status = False

  def get_status(self):
    return self.status


class Event():
  def __init__(self,device,action,time):
    self.device = device
    self.action = action
    self.time = time

  def execute(self):
    if self.action == "turn_on":
      self.device.turn_on()
    elif self.action == "turn_off":
      self.device.turn_off()
    elif self.action == "toggle":
      self.device.toggle()


class Hub():
  def __init__(self):
    self.__devices = {}
    self.__events = []
    self.__log = []

  def register_device(self,device):
    if device.id not in self.__devices:
      self.__devices[device.id] = device
      return True
    return False

  def get_device(self,id):
    for did,device in self.__devices.items():
      if did == id:
        return device
    return None

  def schedule_event(self,device_id,action,time):
    device = self.__devices.get(device_id,None)
    if device is not None:
      event = Event(device,action,time)
      self.__events.append(event)
      return True
    return False

  def run_scheduled_events(self,time=10):
    executed = []
    for event in self.__events:
      if event.time <= time:
        event.execute()
        executed.append(event)
    
    for event in executed:
      self.__events.remove(event)
      

  def voice_command(self,command):
    words = command.lower().split()

    if 'on' in words:
      action = "turn_on"
    elif 'off' in words:
      action = 'turn_off'
    elif 'unlock' in words:
      action = 'turn_on'
    elif 'lock' in words:
      action = 'turn_off'
    else:
      return False

    
    for device in self.__devices.values():  
        
        if device.location.lower() in command.lower():
            
            if "light" in words and isinstance(device, Light):
                if action == "turn_on":
                    device.turn_on()
                elif action == "turn_off":
                    device.turn_off()
                self.__log.append(f"{device.name} {action}ed")
                return True
                
            elif "thermostat" in words and isinstance(device, Thermostat):
                if action == "turn_on":
                    device.turn_on()
                elif action == "turn_off":
                    device.turn_off()
                self.__log.append(f"{device.name} {action}ed")
                return True
                
            elif "lock" in words and isinstance(device, SmartLock):
                if action == "turn_on":
                    device.turn_on()  
                elif action == "turn_off":
                    device.turn_off()  
                self.__log.append(f"{device.name} {action}ed")
                return True
    
    return False  

  def get_logs(self):
    return self.__log


# The Problem statement has too many flaws and rules that contradict with each other