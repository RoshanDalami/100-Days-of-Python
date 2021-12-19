logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
#addition
def add(num1,num2):
    return num1+num2

#Subtraction
def sub(num1,num2):
    return num1-num2

#multiply
def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations = {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}

def calculator():
    run_again = True
    num1 = float(input("What's the first number: "))


    for key in operations:
            print(key)



    while run_again :
        operation_symbol = input("pick an operation: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f" {num1} {operation_symbol} {num2} = {answer} ")
        continue_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit : ")

        if(continue_again == 'n'):
            run_again = False
            calculator()
        else:
            num1 = answer
            

calculator()

# num3 = int(input("What's the next number: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(answer,num3)
# print(f" {answer} {operation_symbol} {num3} = {second_answer} ")
