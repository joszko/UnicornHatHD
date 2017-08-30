import pyowm


def weather_api_call(apiKey, locationID):

    owm = pyowm.OWM(apiKey)
    observation = owm.weather_at_id(locationID)
    w = observation.get_weather()
    return w.get_temperature(unit='celsius')['temp']

