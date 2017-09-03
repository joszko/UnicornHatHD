import time
import draw_digits
import get_weather
try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

unicorn.rotation(0)
unicorn.brightness(1)

run_once = 0

try:
    while True:

        for x in range(0, 16):
            for y in range(4, 11):
                unicorn.set_pixel(x, y, 0, 0, 0)

        time.sleep(1.0)

        # draw time
        draw_digits.draw_digit(time.strftime('%H')[0], 15, 5, 255, 0, 0)
        draw_digits.draw_digit(time.strftime('%H')[1], 11, 5, 255, 0, 0)
        draw_digits.draw_digit(time.strftime('%M')[0], 6, 5, 255, 0, 0)
        draw_digits.draw_digit(time.strftime('%M')[1], 2, 5, 255, 0, 0)
        draw_digits.draw_seconds()

        if run_once == 0:
            temp = get_weather.weather_api_call('fd46da3e11c314e9ff7de4dffa655c1e', 3099424)
            run_once = 1

        if time.strftime('%S') == '59':
            get_weather.draw_temperature(str(int(temp)))

        unicorn.show()

except KeyboardInterrupt:
    unicorn.off()