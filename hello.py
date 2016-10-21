def sum(*numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum
print(sum(3))
print(sum(1,2))

#Skipping negative number 
def sum(*numbers):
	sum = 0
	for number in numbers:
		if number < 0:
			continue
		sum += number
	return sum

print (sum(1))
print(sum(2,4,-23))

#multiply
def multiply(*numbers):
	multiply = 1
	for number in numbers:
		multiply *= number
	return multiply
print multiply(2,3)
