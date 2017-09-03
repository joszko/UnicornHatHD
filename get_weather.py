import pyowm
import draw_digits

try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


def weather_api_call(api_key, location_id):

    owm = pyowm.OWM(api_key)
    observation = owm.weather_at_id(location_id)
    w = observation.get_weather()
    return w.get_temperature(unit='celsius')['temp']

    # print(w.get_status())

def draw_temperature(temp):

    for x in range(0, 16):
        for y in range(4, 11):
            unicorn.set_pixel(x, y, 0, 0, 0)

    draw_digits.draw_digit(temp[:1], 12, 5, 255, 0, 0)
    draw_digits.draw_digit(temp[1:], 8, 5, 255, 0, 0)

    for x in range(3, 5):
        for y in range(5, 7):
            unicorn.set_pixel(x, y, 255, 0, 0)