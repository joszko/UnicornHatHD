import time
import draw_digits
import get_weather
try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

unicorn.rotation(270)
unicorn.brightness(1)


def draw_time():
    # first digit of hour

    y_value = 5

    if time.strftime('%H')[0] == '0':
        draw_digits.draw_zero(15, y_value, 255, 0, 0)
    elif time.strftime('%H')[0] == '1':
        draw_digits.draw_one(15, y_value, 255, 0, 0)
    elif time.strftime('%H')[0] == '2':
        draw_digits.draw_two(15, y_value, 255, 0, 0)

    # second digit of hour
    if time.strftime('%H')[1] == '0':
        draw_digits.draw_zero(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '1':
        draw_digits.draw_one(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '2':
        draw_digits.draw_two(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '3':
        draw_digits.draw_three(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '4':
        draw_digits.draw_four(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '5':
        draw_digits.draw_five(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '6':
        draw_digits.draw_six(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '7':
        draw_digits.draw_seven(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '8':
        draw_digits.draw_eight(11, y_value, 255, 0, 0)
    elif time.strftime('%H')[1] == '9':
        draw_digits.draw_nine(11, y_value, 255, 0, 0)

    # first digit of minutes
    if time.strftime('%M')[0] == '0':
        draw_digits.draw_zero(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '1':
        draw_digits.draw_one(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '2':
        draw_digits.draw_two(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '3':
        draw_digits.draw_three(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '4':
        draw_digits.draw_four(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '5':
        draw_digits.draw_five(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '6':
        draw_digits.draw_six(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '7':
        draw_digits.draw_seven(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '8':
        draw_digits.draw_eight(6, y_value, 255, 0, 0)
    elif time.strftime('%M')[0] == '9':
        draw_digits.draw_nine(6, y_value, 255, 0, 0)

    # first digit of minutes
    if time.strftime('%M')[1] == '0':
        draw_digits.draw_zero(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '1':
        draw_digits.draw_one(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '2':
        draw_digits.draw_two(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '3':
        draw_digits.draw_three(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '4':
        draw_digits.draw_four(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '5':
        draw_digits.draw_five(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '6':
        draw_digits.draw_six(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '7':
        draw_digits.draw_seven(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '8':
        draw_digits.draw_eight(2, y_value, 255, 0, 0)
    elif time.strftime('%M')[1] == '9':
        draw_digits.draw_nine(2, y_value, 255, 0, 0)

    # seconds - one dot = 5 seconds
    sec = int(round(int(time.strftime('%S'))/5, 0))

    if sec == 0:
        for i in range(2, 13):
            unicorn.set_pixel(i, 13, 0, 0, 0)
            unicorn.set_pixel(i, 2, 0, 0, 0)
    elif sec == 1:
        unicorn.set_pixel(13, 13, 0, 255, 0)
        unicorn.set_pixel(13, 2, 0, 255, 0)
    else:
        unicorn.set_pixel(13, 13, 0, 255, 0)
        unicorn.set_pixel(13, 2, 0, 255, 0)
        for dot in range(1, sec):
            unicorn.set_pixel(13 - dot, 13, 0, 255, 0)
            unicorn.set_pixel(13 - dot, 2, 0, 255, 0)


def draw_temperature():

        temp = str(int(get_weather.weather_api_call('fd46da3e11c314e9ff7de4dffa655c1e', 3099424)))

        if temp[:1] == '0':
            draw_digits.draw_zero(12, 11, 255, 0, 0)
        elif temp[:1] == '1':
            draw_digits.draw_one(12, 11, 255, 0, 0)
        elif temp[:1] == '2':
            draw_digits.draw_two(12, 11, 255, 0, 0)
        elif temp[:1] == '3':
            draw_digits.draw_three(12, 11, 255, 0, 0)
        elif temp[:1] == '4':
            draw_digits.draw_four(12, 11, 255, 0, 0)
        elif temp[:1] == '5':
            draw_digits.draw_five(12, 11, 255, 0, 0)
        elif temp[:1] == '6':
            draw_digits.draw_six(12, 11, 255, 0, 0)
        elif temp[:1] == '7':
            draw_digits.draw_seven(12, 11, 255, 0, 0)
        elif temp[:1] == '8':
            draw_digits.draw_eight(12, 11, 255, 0, 0)
        elif temp[:1] == '9':
            draw_digits.draw_nine(12, 11, 255, 0, 0)

        if temp[1:] == '0':
            draw_digits.draw_zero(8, 11, 255, 0, 0)
        elif temp[1:] == '1':
            draw_digits.draw_one(8, 11, 255, 0, 0)
        elif temp[1:] == '2':
            draw_digits.draw_two(8, 11, 255, 0, 0)
        elif temp[1:] == '3':
            draw_digits.draw_three(8, 11, 255, 0, 0)
        elif temp[1:] == '4':
            draw_digits.draw_four(8, 11, 255, 0, 0)
        elif temp[1:] == '5':
            draw_digits.draw_five(8, 11, 255, 0, 0)
        elif temp[1:] == '6':
            draw_digits.draw_six(8, 11, 255, 0, 0)
        elif temp[1:] == '7':
            draw_digits.draw_seven(8, 11, 255, 0, 0)
        elif temp[1:] == '8':
            draw_digits.draw_eight(8, 11, 255, 0, 0)
        elif temp[1:] == '9':
            draw_digits.draw_nine(8, 11, 255, 0, 0)

        unicorn.set_pixel(4, 11, 255, 0, 0)
        unicorn.set_pixel(4, 12, 255, 0, 0)
        unicorn.set_pixel(3, 11, 255, 0, 0)
        unicorn.set_pixel(3, 12, 255, 0, 0)

run_once = 0

while True:

    for x in range(0,16):
        for y in range(4,11):
            unicorn.set_pixel(x, y, 0, 0, 0)

    time.sleep(1.0)

    # if run_once == 0:
    #     draw_temperature()
    #     run_once = 1

    draw_time()

    # if time.strftime('%M:%S') == '59:59':
    #     draw_temperature()

    unicorn.show()
