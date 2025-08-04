def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return "Error: Can't divide by zero"
	return a / b

while True:
	try:
		num1 = float(input("Enter first number: ").strip())
		num2 = float(input("Enter second number: ").strip())
	except ValueError:
		print("Error: Invalid input. Please enter numbers only.")
		continue

	print("Choose operation:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")

	choice = input("Select an option (1-4): ").strip()

	if choice == "1":
		result = add(num1, num2)
	elif choice == "2":
		result = subtract(num1, num2)
	elif choice == "3":
		result = multiply(num1, num2)
	elif choice == "4":
		result = divide(num1, num2)
	else:
		result = "Error: Please select a valid operation (1–4)"
	
	print("Output:", result)

	again = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
	if again != 'yes':
		print("Goodbye!")
		break