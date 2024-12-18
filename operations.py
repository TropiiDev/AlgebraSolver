from fractions import Fraction

def point_slope_form(x, y, slope):
    if str(y).startswith('-') and str(x).startswith('-'):
        new_y = int(str(y).split('-')[1])
        new_x = int(str(x).split('-')[1])

        return f"y+{new_y}={slope}(x+{new_x})"
    elif str(y).startswith('-'):
        new_y = int(str(y).split('-')[1])

        return f"y+{new_y}={slope}(x-{x})"
    elif str(x).startswith('-'):
        new_x = int(str(x).split('-')[1])

        return f"y-{y}={slope}(x+{new_x})"
    else:
        return f"y-{y}={slope}(x-{x})"

def slope_intercept_form(x, y, slope):
    y_intercept = (slope * -x) + y

    if str(y_intercept).startswith('-') is False:
        y_intercept = f"+{y_intercept}"

    return f"y={slope}x{y_intercept}"

def find_slope(x, y, x_two, y_two):
    return str(Fraction((y_two - y) / (x_two - x)).limit_denominator(100))