"""
def power(a):
    b=int(input("enter the power:"))
    p=(a**b)
    print(f"power of the number is :{p}")
    return p
power(2)
"""
#--------------------problem one---------------#
"""
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Error"

def calculator():
    print("select your choice:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        ch = input("Enter the operation number (1-5): ")

        if ch == '5':
            print("No operation.")
            break

        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if ch == '1':
            res = add(a,b)
            print("Result:", res)
        elif ch == '2':
            res = subtract(a,b)
            print("Result:",res)
        elif ch == '3':
            res = multiply(a,b)
            print("Result:", res)
        elif ch == '4':
            res = divide(a,b)
            print("Result:", res)
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

calculator()

"""

#-----------------------Function to check the status of light and turn it on/off------------------------------

"""

def light(l_status):
    if l_status == "on":
        return "off"
    elif l_status == "off":
        return "on"
    else:
        return "Damaged"
    

l_status=input("Enter the status of light:")
print("current light status is:",l_status)

l_status = light(l_status)
print("New light status:", l_status)

"""

#-------------------------------------problem three-----------------------------------------


"""
l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))

def cal_area(l, w):
    area = l * w
    return area

def cal_perimeter(l, w):
    perimeter = 2 * (l + w)
    return perimeter


area = cal_area(l, w)
perimeter = cal_perimeter(l, w)

print("Area:", area)
print("Perimeter:", perimeter)
"""

