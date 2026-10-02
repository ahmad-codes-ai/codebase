import httpx


def get_coordinates(city):

  response = httpx.get("https://geocoding-api.open-meteo.com/v1/search",params={'name':city, 'count':1})

  if response.status_code == 200:
    data = response.json()
    result = []
    result.append(data['results'][0]["latitude"])
    result.append(data['results'][0]["longitude"])
    return result

  else:
    return response.status_code



def get_weather(coordinate):
  if type(coordinate) is list:

    response = httpx.get("https://api.open-meteo.com/v1/forecast",
                         params={'latitude': coordinate[0], 
                                 'longitude': coordinate[-1],
                                 'daily': "temperature_2m_max,temperature_2m_min",
                                 'forecast_days' : 2
                                 }
                         )

    if response.status_code == 200:
      data = response.json()
      print(f"Weather Forcast is: \n ")
      print('-'*50)
      dates = data['daily']['time']
      max_temp = data['daily']['temperature_2m_max']
      min_temp = data['daily']['temperature_2m_min']

    
      for index,(date,max,min) in enumerate(zip(dates,max_temp,min_temp)):
        print(f"Day: {index+1} \nDate: {date} \nMax: {max} \nMin: {min}")
        print('-'*50)


    else:
      print(response.status_code)

  else:
    print("Invalid coordinates")



user = input("Enter city: ")
result = get_coordinates(user)
get_weather(result)