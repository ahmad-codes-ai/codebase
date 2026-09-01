'''
Easy Problem 3 – Weather Station
Context A weather station collects daily temperature and humidity readings.

Task Create a DailyReport class with:

Attributes: date (string), temperature (float), humidity (int).
Create a WeatherStation class that:

Has a list of DailyReport objects.
Methods: add_report(report), average_temperature() – returns average of all temps.
get_humidity(date) – returns humidity for a given date.
Sample Usage

station = WeatherStation()
station.add_report(DailyReport("2026-08-01", 25.5, 60))
station.add_report(DailyReport("2026-08-02", 26.0, 55))
print(station.average_temperature())  # 25.75
print(station.get_humidity("2026-08-01"))  # 60
'''

class DailyReport:
  def __init__(self,date,temp,hum):
    self.date = date
    self.temp = temp
    self.humidity = hum

class WeatherStation:
  def __init__(self):
    self.reports = []

  def add_report(self,report):
    if report not in self.reports:
      self.reports.append(report)
      return True
    else:
      return False

  def average_temperature(self):
    s = 0
    for i in self.reports:
       s+=i.temp

    avg = s/len(self.reports)
    return avg

  def get_humidity(self,date):
    for i in self.reports:
      if i.date == date:
        return i.humidity
    return None

station = WeatherStation()
station.add_report(DailyReport("2026-08-01", 25.5, 60))
station.add_report(DailyReport("2026-08-02", 26.0, 55))
print(station.average_temperature())  # 25.75
print(station.get_humidity("2026-08-01"))  # 60