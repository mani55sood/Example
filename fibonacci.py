num = int(input("numbers enter" ))
def fib(num):
 num1 = 0
 num2 = 1
 print (num1)
 print (num2)
 count = 2
 while count < num:
 	num3 = num1+num2
 	print (num3)
 	count = count + 1
 	num1 = num2
 	num2 = num3
 	return 1
 	fib (num)