import requests


def get_weather_conditions(city, date):
        weather_url = f"KCAzFut3rqsg==&city={city}%20Rebeccaberg&date={date}"
        response = requests.get(weather_url)
        if response.status_code == 200:
             try:
                weather_data = response.json()
                return weather_data
             except ValueError as e:
                  print(e)
                  return None
        else:
            print("Error:", response.status_code)
            return None


def calculate_distance(user_latitude: str, user_longitude: str, event_latitude: str, event_longitude:str) -> None:
    distance_url = "code=IAKvV2EvJau8Y3IcQ==&latitude1={}&longitude1={}&latitude2={}&longitude2={}".format(user_latitude, user_longitude, event_latitude, event_longitude)
    params = {
        'user_latitude': user_latitude,
        'user_longitude': user_longitude,
        'event_latitude': event_latitude,
        'event_longitude': event_longitude
    }
    response = requests.get(distance_url, params=params)
    if response.status_code == 200:
        try:
            distance_data = response.json()
            return distance_data
        except ValueError as e:
            print(e)
            return None
    else:
        print("Error:", response.status_code)
        return None

