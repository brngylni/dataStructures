numbers = []
def addition(numbers):
	result	=	0
	count	=	len(numbers)
	x		=	0
	while x < count:
		result	=	result + numbers[x]
		x += 1
	return result
def substraction(numbers):
	result	=	numbers[0]
	count	=	len(numbers)
	x		=	1
	while x < count:
		result	=	result - numbers[x]
		x += 1
	return result
def multiplication(numbers):
	x		=	0
	result	=	1
	count	=	len(numbers)

	while x < count:
		result	=	result * numbers[x]
		x += 1
	return result
def division(numbers):
	x		=	1
	result	=	numbers[0]
	count	=	len(numbers)

	while x < count:
		result	=	result // numbers[x]
		x += 1
	return result
def modulus(numbers):
	x		=	1
	result	=	numbers[0]
	count	=	len(numbers)

	while x < count:
		result	=	result % numbers[x]
		x += 1
	return result
print(' 1. Addition \n 2. Substracion \n 3. Multiplication \n 4. Division \n 5. Modulus\n')
operation = input('Enter the number of operation you want to do :')
if	 operation =='1':
	count = int(input('Enter how much numbers you want to sum : '))
	while count >= 1 :
		number =	int(input('Give me a number :'))
		numbers.append(number)
		count -= 1
	result	=  addition(numbers)
	print('Here is the our result : ' , result)
elif operation == '2':
	count = int(input('Enter how much numbers you want to substract : '))
	while count >= 1:
		number = int(input('Give me a number :'))
		numbers.append(number)
		count -= 1
	result	=	substraction(numbers)
	print('Here is the our result : ' , result)
elif operation == '3':
	count = int(input('Enter how much numbers you want to multiply :'))
	while count >= 1:
		number = int(input('Give me a number :'))
		numbers.append(number)
		count -= 1
	result = multiplication(numbers)
	print('Here is the our result : ' , result)
elif operation == '4':
	count = int(input('Enter how much numbers you want to divide :'))
	while count >= 1:
		number = int(input('Give me a number :'))
		numbers.append(number)
		count -= 1
	result = division(numbers)
	print('Here is the our result : ' , result)
elif operation == '5':
	count = int(input('Enter how much numbers you want to take modulus :'))
	while count >= 1:
		number = int(input('Give me a number :'))
		numbers.append(number)
		count -= 1
	result = modulus(numbers)
	print('Here is the our result : ' , result)
else:
	print('You entered an unvalid number.')

		