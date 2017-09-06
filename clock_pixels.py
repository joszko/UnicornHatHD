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

temp, status = get_weather.weather_api_call('fd46da3e11c314e9ff7de4dffa655c1e', 6255152)

icons = {'01d': r'./icons/clear-day.png', '01n': r'./icons/clear-night.png',
         '02d': r'./icons/partly-cloudy-day.png', '02n': r'./icons/partly-cloudy-night.png',
         '03d': r'./icons/cloudy.png', '03n': r'./icons/cloudy.png',
         '04d': r'./icons/cloudy.png', '04n': r'./icons/cloudy.png',
         '09d': r'./icons/rain.png', '09n': r'./icons/rain.png',
         '10d': r'./icons/rain.png', '10n': r'./icons/rain.png',
         '11d': r'./icons/lightning-icon.png', '11n': r'./icons/lightning-icon.png',
         '13d': r'./icons/snow.png', '13n': r'./icons/snow.png',
         '50d': r'./icons/fog.png', '50n': r'./icons/fog.png'}

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
            temp, status = get_weather.weather_api_call('fd46da3e11c314e9ff7de4dffa655c1e', 6255152)

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
                        time.sleep(0.15)

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
