####################### Calculator Project, Functions with outputs #######################
# def format_name(f_name, l_name):
#     ## DocString
#     """Take a first name and last name and return the title case version"""
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"


# output = format_name("ozod", "oTamIRZaev")
# print(output)



##############################################################################################################################
def multiply(number1, number2):
    nextNum = number1 * number2
    print(f"{number1} * {number2} = {nextNum}")
    return nextNum

def divide(number1, number2):
    nextNum = number1 / number2
    print(f"{number1} / {number2} = {nextNum}")
    return nextNum

def add(number1, number2):
    nextNum = number1 + number2
    print(f"{number1} + {number2} = {nextNum}")
    return nextNum

def subtract(number1, number2):
    nextNum = number1 - number2
    print(f"{number1} - {number2} = {nextNum}")
    return nextNum


yesOrNo = 'n'
nextNumber = 0

## create a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
while True:
    num1 = nextNumber
    if (yesOrNo == 'n'):
        num1 = float(input("What is the first number?: "))
    
    # print("+\n-\n*\n/")
    for operation in operations:
        print(operation)
    operation = str(input("Pick an operation: "))
    num2 = float(input("What is the next number?: "))
    nextNumber = operations[operation](num1, num2)


    ## ask if they want to continue
    yesOrNo = str(input(f"Type 'y' to continue calculating with {nextNumber} or type 'n' to start a new calculation: "))
    if yesOrNo == 'n':
        print("\n" * 30)
        continue


