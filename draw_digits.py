try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


def draw_zero(x, y, r, g, b):

    for y_pixel in range(y, y + 5):
        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

    for y_pixel in range(y, y + 5):
        unicorn.set_pixel(x, y_pixel, r, b, g)
        unicorn.set_pixel(x - 2, y_pixel, r, b, g)

    unicorn.set_pixel(x - 1, y, r, b, g)
    unicorn.set_pixel(x - 1, y + 4, r, b, g)


def draw_one(x, y, r, g, b):

    for y_pixel in range(y, y + 5):
        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

    for y_pixel in range(y, y + 5):
        unicorn.set_pixel(x - 2, y_pixel, r, b, g)

    unicorn.set_pixel(x-1, y + 1, r, b, g)
    unicorn.set_pixel(x, y + 2, r, b, g)


def draw_two(x, y, r, g, b):

    for y_pixel in range(y, y + 5):
        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

    for x_pixel in range(x-2, x + 1):
        unicorn.set_pixel(x_pixel, y,  r, b, g)
        unicorn.set_pixel(x_pixel, y + 2, r, b, g)
        unicorn.set_pixel(x_pixel, y + 4, r, b, g)

    unicorn.set_pixel(x - 2, y + 1, r, b, g)
    unicorn.set_pixel(x, y + 3, r, b, g)


def draw_three(x, y, r, g, b):

    for y_pixel in range(y, y + 5):
        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

    for y_pixel in range(y, y + 5):
        unicorn.set_pixel(x - 2, y_pixel, r, b, g)

    for x_pixel in range(x - 2, x + 1):
        unicorn.set_pixel(x_pixel, y, r, b, g)
        unicorn.set_pixel(x_pixel, y + 4, r, b, g)

    unicorn.set_pixel(x - 1, y + 2, r, b, g)


def draw_four(x, y, r, g, b):

    for y_pixel in range(y, y + 5):
        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

    for y_pixel in range(y, y + 5):
        unicorn.set_pixel(x - 2, y_pixel, r, b, g)

    for y_pixel in range(y, y + 3):
        unicorn.set_pixel(x, y_pixel, r, b, g)

    for x_pixel in range(x - 2, x + 1):
        unicorn.set_pixel(x_pixel, y + 2, r, b, g)


def draw_five(x, y, r, g, b):

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


def draw_six(x, y, r, g, b):

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


def draw_seven(x, y, r, g, b):

    for y_pixel in range(y, y + 5):
        for x_pixel in range(x - 2, x + 1):
            unicorn.set_pixel(x_pixel, y_pixel, 0, 0, 0)

    for x_pixel in range(x - 2, x + 1):
        unicorn.set_pixel(x_pixel, y, r, b, g)

    for y_pixel in range(y, y + 5):
        unicorn.set_pixel(x - 2, y_pixel, r, b, g)


def draw_eight(x, y, r, g, b):

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


def draw_nine(x, y, r, g, b):

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
