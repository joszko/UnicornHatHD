import time
import draw_digits
import get_weather
from PIL import Image
try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

unicorn.brightness(1)

width, height = unicorn.get_shape()

temp, status = get_weather.weather_api_call('fd46da3e11c314e9ff7de4dffa655c1e', 3099424)

icons = {'clear sky': r'./icons/clear-day.png',
         'few clouds': r'./icons/partly-cloudy-day.png',
         'scattered clouds': r'./icons/cloudy.png',
         'broken clouds': r'./icons/cloudy.png',
         'shower rain': r'./icons/rain.png',
         'rain': r'./icons/rain.png',
         'thunderstorm': r'./icons/lightning-icon.png',
         'snow': r'./icons/snow.png',
         'mist': r'./icons/fog.png'}

try:
    while True:
        unicorn.rotation(270)
        for x in range(0, 16):
            for y in range(0, 16):
                unicorn.set_pixel(x, y, 0, 0, 0)

        time.sleep(1.0)

        # draw time
        draw_digits.draw_digit(time.strftime('%H')[0], 15, 5, 255, 0, 0)
        draw_digits.draw_digit(time.strftime('%H')[1], 11, 5, 255, 0, 0)
        draw_digits.draw_digit(time.strftime('%M')[0], 6, 5, 255, 0, 0)
        draw_digits.draw_digit(time.strftime('%M')[1], 2, 5, 255, 0, 0)
        draw_digits.draw_seconds()

        # update weather data
        if time.strftime('%M') == '59':
            temp, status = get_weather.weather_api_call('fd46da3e11c314e9ff7de4dffa655c1e', 3099424)

        # draw weather data
        if int(time.strftime('%S')) % 30 == 0:

            img = Image.open(icons[status])
            unicorn.rotation(0)
            for o_x in range(int(img.size[0] / width)):
                for o_y in range(int(img.size[1] / height)):

                    valid = False
                    for x in range(width):
                        for y in range(height):
                            pixel = img.getpixel(((o_x * width) + y, (o_y * height) + x))
                            r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
                            if r or g or b:
                                valid = True
                            unicorn.set_pixel(x, y, r, g, b)
                    if valid:
                        unicorn.show()
                        time.sleep(0.2)

            for x in range(0, 16):
                for y in range(0, 16):
                    unicorn.set_pixel(x, y, 0, 0, 0)

            unicorn.rotation(270)

            get_weather.draw_temperature(temp)
            time.sleep(1.0)

        unicorn.show()

except KeyboardInterrupt:
    unicorn.clear()
    unicorn.off()
