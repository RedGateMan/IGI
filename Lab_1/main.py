from helpers import Operations

print("Hello, World!")


def calc(first_int, second_int, operation):
	match (operation):
		case (Operations.ADD):
			print("Sum result: ", first_int + second_int)
		case (Operations.SUB):
			print("Sub result(first_int - second_int): ", first_int - second_int)
		case (Operations.MULT):
			print("Mul result: ", first_int * second_int)
		case (Operations.DIV):
			try:
				print("Div result(first_int / second_int): ", first_int / second_int)
			except ZeroDivisionError:
				print("Division by zero!")


try:
	first_int = int(input("Enter A: "))
	second_int = int(input("Enter B: "))
	operation = Operations(input("Chose operation (add, sub, mult, div): "))
	calc(first_int, second_int, operation)
except ValueError:
	print("Invalid input!")


def even_list(array):
	even_array = [x for x in array if x % 2 == 0]
	return even_array


try:
	array = list(map(int, input("Input your array(divided by spaces)\n").split()))
	print(even_list(array))
except ValueError:
	print("Invalid input!")
