import time
import colorsys
from random import randint
try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


def draw_digit(digit, x, y, r, g, b):

    if digit == '0':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for y_pixel in range(y, y + 5):
            unicorn.set_pixel(x, y_pixel, r, b, g)
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

        unicorn.set_pixel(x - 1, y, r, b, g)
        unicorn.set_pixel(x - 1, y + 4, r, b, g)

    elif digit == '1':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for y_pixel in range(y, y + 5):
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

        unicorn.set_pixel(x - 1, y + 1, r, b, g)
        unicorn.set_pixel(x, y + 2, r, b, g)

    elif digit == '2':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y, r, b, g)
            unicorn.set_pixel(x_pixel, y + 2, r, b, g)
            unicorn.set_pixel(x_pixel, y + 4, r, b, g)

        unicorn.set_pixel(x - 2, y + 1, r, b, g)
        unicorn.set_pixel(x, y + 3, r, b, g)

    elif digit == '3':
        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for y_pixel in range(y, y + 5):
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y, r, b, g)
            unicorn.set_pixel(x_pixel, y + 4, r, b, g)

        unicorn.set_pixel(x - 1, y + 2, r, b, g)

    elif digit == '4':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for y_pixel in range(y, y + 5):
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

        for y_pixel in range(y, y + 3):
            unicorn.set_pixel(x, y_pixel, r, b, g)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y + 2, r, b, g)

    elif digit == '5':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y, r, b, g)
            unicorn.set_pixel(x_pixel, y + 2, r, b, g)
            unicorn.set_pixel(x_pixel, y + 4, r, b, g)

        for y_pixel in range(y, y + 3):
            unicorn.set_pixel(x, y_pixel, r, b, g)

        for y_pixel in range(y + 2, y + 5):
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

    elif digit == '6':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y, r, b, g)
            unicorn.set_pixel(x_pixel, y + 2, r, b, g)
            unicorn.set_pixel(x_pixel, y + 4, r, b, g)

        for y_pixel in range(y, y + 3):
            unicorn.set_pixel(x, y_pixel, r, b, g)

        for y_pixel in range(y + 2, y + 5):
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

        unicorn.set_pixel(x, y + 3, r, b, g)

    elif digit == '7':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y, r, b, g)

        for y_pixel in range(y, y + 5):
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

    elif digit == '8':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y, r, b, g)
            unicorn.set_pixel(x_pixel, y + 2, r, b, g)
            unicorn.set_pixel(x_pixel, y + 4, r, b, g)

        for y_pixel in range(y, y + 5):
            unicorn.set_pixel(x, y_pixel, r, b, g)
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

    elif digit == '9':

        for y_pixel in range(y, y + 5):
            for x_pixel in range(x - 2, x + 1):
                unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y, r, b, g)
            unicorn.set_pixel(x_pixel, y + 2, r, b, g)
            unicorn.set_pixel(x_pixel, y + 4, r, b, g)

        for y_pixel in range(y, y + 5):
            unicorn.set_pixel(x, y_pixel, r, b, g)
            unicorn.set_pixel(x - 2, y_pixel, r, b, g)

        unicorn.set_pixel(x, y + 3, 0, 0, 0)

def gradient(x, y, step):
    g = x * 16
    b = y * 16
    r = 255 - (x * 16)

    return (r, g, b)


def draw_seconds():
    step = 0
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

            r = gradient(13 - dot, 13,step)[0]
            b = gradient(13 - dot, 13,step)[2]
            g = gradient(13 - dot, 13,step)[1]

            unicorn.set_pixel(13 - dot, 13, r, g, b)
            unicorn.set_pixel(13 - dot, 2, r, g, b)

        step += 2