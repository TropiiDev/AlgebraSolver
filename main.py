from operations import *

while True:
    mathematical_operation = str(input("""
        Welcome to the Python Algebra Solver!
        
        Please input your desired operation below..
        
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

        correct = input(f"The following formula is: {point_slope}\nIs this correct? (y/n) ")

        if correct == "y":
            slope_intercept = slope_intercept_form(x, y, slope)

            correct = input(f"The slope intercept formula is: {slope_intercept}.\nIs this correct? (y/n) ")

            if correct == "y":
                do_continue = input("Do you want to continue with this program? (y/n) ")

                if do_continue == 'y':
                    print("Okay!")
                else:
                    print("Bye bye!")
                    break
            else:
                print("Something must have gone wrong.. Add an error to the Github.")
                break
        if correct == "n":
            print("Something must have gone wrong.. Add an error to the Github.")
            break
    else:
        print("The operation inputted has either not been created or is not available. Try again.")