from operations import *
import time

while True:
    mathematical_operation = str(input("""
        Welcome to the Python Algebra Solver!
        
        Please input your desired operation below..
        
        If there are any incorrect answers please make a report here: https://github.com/TropiiDev/AlgebraSolver/issues
        
        The following operations are supported with this script:
            - Graphing : Using y=mx+b
            - Conversion : From point slope form to slope intercept formula
            - Slope : Get the slope from two points on a graph
            
        example: graphing
        
    Option: 
    """))

    if mathematical_operation == "graphing":
        print("This feature has not been implemented yet.. Try again.")
    elif mathematical_operation == "conversion":
        slope = int(input("Please enter the slope: "))
        x = int(input("Please enter the X: "))
        y = int(input("Please enter the Y: "))

        point_slope = point_slope_form(x, y, slope)

        print(f"The point slope formula is: {point_slope}")

        slope_intercept = slope_intercept_form(x, y, slope)

        print(f"The slope intercept formula is: {slope_intercept}.")

        do_continue = input("Do you want to continue with this program? (y/n) ")

        if do_continue == 'y':
            print("Okay!")
        else:
            print("Bye bye!")
            break

    elif mathematical_operation == "slope":
        point_one = input("Please enter the first point: (Example: 3 6) ")
        point_two = input("Please enter the second point: (Example: -2 5) ")

        point_one_int = point_one.split(" ")
        x_one = int(point_one_int[0])
        y_one = int(point_one_int[1])

        point_two_int = point_two.split(" ")
        x_two = int(point_two_int[0])
        y_two = int(point_two_int[1])

        slope = find_slope(x_one, y_one, x_two, y_two)

        print(f"The slope is: {slope}")
        time.sleep(2)

        do_continue = input("Do you want to continue with this program? (y/n) ")

        if do_continue == 'y':
            print("Okay!")
        else:
            print("Bye bye!")
            break
    else:
        print("The operation entered has either not been created or is not available. Try again.")
        print("The program will continue in 2 seconds.")
        time.sleep(2)
