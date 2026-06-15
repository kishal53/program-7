import datetime
import time
import math
import random
import string
import uuid
import importlib
import file_module

def Datetime_operation():
     while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                now = datetime.datetime.now()
                print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
            case 2: 
                date1 = input("Enter the first date (YYYY-MM-DD): ")
                date2 = input("Enter the second date (YYYY-MM-DD): ")
                try:
                    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
                    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
                    diff = abs((d2 - d1).days)
                    print(f"Difference: {diff} days")
                except ValueError:
                    print("Invalid date format! Please use YYYY-MM-DD.")
            case 3: 
                date_str = input("Enter a date (YYYY-MM-DD): ")
                print("Available formats:")
                print("  1. DD-MM-YYYY  (e.g. 04-01-2025)")
                print("  2. MM/DD/YYYY  (e.g. 01/04/2025)")
                print("  3. DD Month YYYY  (e.g. 04 January 2025)")
                print("  4. Custom (type your own, e.g. %d/%m/%Y)")
                choice = input("Choose format (1/2/3/4): ").strip()

                format_map = {
                    "1": "%d-%m-%Y",
                    "2": "%m/%d/%Y",
                    "3": "%d %B %Y",
                }

                try:
                    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                    if choice in format_map:
                        print("Formatted Date:", d.strftime(format_map[choice]))
                    elif choice == "4":
                            custom_fmt = input("Enter your format (e.g. %d/%m/%Y): ").strip()
                            print("Formatted Date:", d.strftime(custom_fmt))
                    else:
                            print("Invalid choice.")
                except ValueError:
                        print("Invalid date format! Please use YYYY-MM-DD.")
            case 4: 
                print("Stopwatch started. Press Enter to stop...")
                start = time.time()
                input()
                elapsed = round(time.time() - start, 2)
                print(f"Elapsed Time: {elapsed} seconds")
            case 5:
                try:
                    seconds = int(input("Enter countdown time in seconds: "))
                    if seconds <= 0:
                        print("Please enter a positive number.")
                        return
                    print(f"Countdown starting from {seconds} seconds...")
                    for i in range(seconds, 0, -1):
                        print(f"\r  {i} second(s) remaining...", end="", flush=True)
                        time.sleep(1)
                    print("\r  Time's up!                    ")
                except ValueError:
                    print("Invalid input! Please enter a whole number.")
            case 6:
                break
            case _:
                print("Wrong input")
                
                
def  maths_operation():
      while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                try:
                    n = int(input("Enter a number: "))
                    if n < 0:
                        print("Factorial is not defined for negative numbers.")
                    else:
                        print(f"Factorial: {math.factorial(n)}")
                except ValueError:
                    print("Invalid input! Please enter a whole number.")
            case 2:
                try:
                    principal = float(input("Enter principal amount: "))
                    rate      = float(input("Enter rate of interest (in %): "))
                    time      = float(input("Enter time (in years): "))
                    amount    = principal * (1 + rate / 100) ** time
                    print(f"Compound Interest: {amount:.2f}")
                except ValueError:
                    print("Invalid input! Please enter numeric values.")
            case 3:
                    print("Trigonometric functions: sin, cos, tan, cosec, sec, cot")
                    func   = input("Enter function name (e.g. sin): ").strip().lower()
                    try:
                        degree = float(input("Enter angle in degrees: "))
                        radians = math.radians(degree)

                        match func:
                            case "sin":
                                result = math.sin(radians)
                            case "cos":
                                result = math.cos(radians)
                            case "tan":
                                if degree % 180 == 90:
                                    print("tan is undefined at this angle.")
                                    return
                                result = math.tan(radians)
                            case "cosec":
                                s = math.sin(radians)
                                if s == 0:
                                    print("cosec is undefined at this angle.")
                                    return
                                result = 1 / s
                            case "sec":
                                c = math.cos(radians)
                                if c == 0:
                                    print("sec is undefined at this angle.")
                                    return
                                result = 1 / c
                            case "cot":
                                t = math.tan(radians)
                                if t == 0:
                                    print("cot is undefined at this angle.")
                                    return
                                result = 1 / t
                            case _:
                                print("Unknown function. Use: sin, cos, tan, cosec, sec, cot")
                                return

                        print(f"{func}({degree}°) = {round(result, 6)}")

                    except ValueError:
                        print("Invalid input! Please enter a numeric angle.")
            case 4:
                print("Available shapes: square, rectangle, circle, triangle")
                shape = input("Enter shape name: ").strip().lower()

                try:
                    match shape:
                        case "square":
                            side = float(input("Enter side length: "))
                            area = side ** 2
                            print(f"Area of Square: {area:.4f}")

                        case "rectangle":
                            length = float(input("Enter length: "))
                            breadth = float(input("Enter breadth: "))
                            area = length * breadth
                            print(f"Area of Rectangle: {area:.4f}")

                        case "circle":
                            radius = float(input("Enter radius: "))
                            area = math.pi * radius ** 2
                            print(f"Area of Circle: {area:.4f}")

                        case "triangle":
                            base   = float(input("Enter base: "))
                            height = float(input("Enter height: "))
                            area = 0.5 * base * height
                            print(f"Area of Triangle: {area:.4f}")

                        case _:
                            print("Unknown shape. Choose: square, rectangle, circle, triangle")

                except ValueError:
                    print("Invalid input! Please enter numeric values.")
            case 5:
                break
            case _:
                print("Invalid choice")
            

      
def Random_data_operation():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                try:
                    low  = int(input("Enter lower bound: "))
                    high = int(input("Enter upper bound: "))
                    if low > high:
                        print("Lower bound must be less than upper bound.")
                        return
                    print(f"Random Number: {random.randint(low, high)}")
                except ValueError:
                    print("Invalid input! Please enter whole numbers.")
                    
                    
            case 2:
                try:
                    size = int(input("Enter how many numbers you want in the list: "))
                    low  = int(input("Enter minimum value: "))
                    high = int(input("Enter maximum value: "))
                    if size <= 0:
                            print("Size must be greater than 0.")
                            return
                    lst = [random.randint(low, high) for _ in range(size)]
                    print(f"Random List: {lst}")
                except ValueError:
                        print("Invalid input! Please enter whole numbers.")                
                
            case 3:
                    try:
                        length = int(input("Enter password length: "))
                        if length < 4:
                            print("Password length must be at least 4.")
                            return
                        # Mix of letters, digits, and special characters
                        chars    = string.ascii_letters + string.digits + string.punctuation
                        password = "".join(random.choices(chars, k=length))
                        print(f"Generated Password: {password}")
                    except ValueError:
                        print("Invalid input! Please enter a whole number.")
                
            case 4:
                    try:
                        length = int(input("Enter OTP length (4-8): "))
                        if length < 4 or length > 8:
                            print("OTP length must be between 4 and 8.")
                            return
                        otp = "".join(random.choices(string.digits, k=length))
                        print(f"Generated OTP: {otp}")
                    except ValueError:
                        print("Invalid input! Please enter a whole number.")
                
                
            case 5:
                break
            case _:
                print("Invalid choice! Please enter a number between 1 and 5.")

def uuid_operation():
        print("\nGenerate Unique Identifiers:")          
        new_uuid = uuid.uuid4()
        print(f"Generated UUID: {new_uuid}")        
                
                
                
def file_operation():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                file_module.create_file()
            case 2:
                file_module.write_file()
            case 3:
                file_module.read_file()
            case 4:
                file_module.append_file()
            case 5:
                break
            case _:
                print("Invalid choice! Please enter a number between 1 and 5.")

def module_attribute():
        print("\nExplore Module Attributes:")
        module_name = input("Enter module name to explore: ").strip()

        try:
            mod   = importlib.import_module(module_name)
            attrs = [a for a in dir(mod) if not a.startswith("__")]

            print(f"Available Attributes in {module_name} module:")
            print(attrs[:8])
            if len(attrs) > 8:
                print(attrs[8:10] + ["..."])

            if len(attrs) > 10:
                see_all = input("See all attributes? (y/n): ").strip().lower()
                if see_all == "y":
                    print(attrs)

        except ModuleNotFoundError:
            print(f"Module '{module_name}' not found.")
            print("Try: math, random, datetime, os, sys, uuid, string")     
                
                
                




print("==========================================")
print("Welcome to the Multy-Utility Toolkit")
print("==========================================")



while True:
    print("Choose an option:")
    print("1. Datetime and time operations")
    print("2. Mathematical Operations")
    print("3. random Data generator")
    print("4. Generate Uniques Identifier(UUID)")
    print("5. File operation (custom module)")
    print("6. Explore Module Attribute(dir())")
    print("7. Exit")

    print("==========================================")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            Datetime_operation()
        case 2:
            maths_operation()
        case 3:
            Random_data_operation()
        case 4:
            uuid_operation()
        case 5:
            file_operation()
        case 6:
            module_attribute()
        case 7:
            break
        case _:
            print("Wrong input")