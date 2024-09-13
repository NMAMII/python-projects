def add(n1,n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2


def divide(n1,n2):
    return n1/n2


def multiply(n1,n2):
    return n1 * n2


def module(n1, n2):
    return n1 % n2


math_op = {
    "+": add,
    "-":subtract,
    "/":divide,
    "*":multiply,
    "%":module
}
calc_logo = '''
 _____________________
|  _________________  |
| | Hello World!  0.| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(calc_logo)
print("Ready to calculate!")
num1 = float(input("Input the first number: "))
on = True
while on:
    num2 = float(input("Input the second number: "))
    op = input("Type just the operation you want to preform from (+ , - , * , % , /): ")
    answer = float(math_op[op](num1, num2))
    print(f"{num1} {op} {num2} = {answer}")
    should_continue = input(f"Do you want to keep doing operation on {answer} y/n? ").lower()
    if should_continue == "y":
        num1 = answer
    elif should_continue == "n":
        new_or_close = input("Do you want start new calculations or close? type 'new' or 'close': ").lower()
        if new_or_close == "new":
            num1 = float(input("Input the first number: "))
        elif new_or_close == 'close':
            print("Thank you.")
            on = False
