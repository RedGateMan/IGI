from helpers import Operations

print("Hello, World!")
first_int = int(input("Enter A: "))
second_int = int(input("Enter B: "))
operation = input("Chose operation (add, sub, mult, div): ")


def calc(first_int, second_int, operation):
    match (operation):
        case (Operations.ADD.value):
            print("Sum result: ", first_int + second_int)
        case (Operations.SUB.value):
            print("Sub result(first_int - second_int): ", first_int - second_int)
        case (Operations.MULT.value):
            print("Mul result: ", first_int * second_int)
        case (Operations.DIV.value):
            try:
                print("Div result(first_int / second_int): ", first_int / second_int)
            except ZeroDivisionError:
                print("Division by zero!")
        case _:
            print("Invalid input!")

calc(first_int, second_int, operation)
