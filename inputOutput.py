# var= int(input("Enter the value:"+" "))
# print(var,type(var))

# var2=eval(input("Enter the value: "))
# print(var2,type(var2))

# wap to print sum of two numbers

# num1=int(input("Enter the number1: "))
# num2= int(input("enter the num2: "))

# add=num1+num2
# print(add)

#wap to print the user full name by taking the first and last name from the user.

# firstName= input("Please enter first name: ")
# lastName= input("please enter last name: ")

# fullName=firstName+lastName



# firstValue= eval(input("Enter the first value: "))
# lastValue=eval(input("Enter the second value: "))

# list1=[firstValue, lastValue]
# print(list1, len(list1))

# tup=eval(input("Enter the value of tuple"))
# print(tup)
# print(tup[::-1])

# Take a dictionary from the user and print the last value of the item
# dict2= eval(input("enter the dict: "))

# poppedItem=dict2.popItem()

# print(poppedItem)
# print(poppedItem[-1])

d1=eval(input("Enter a dictionary: "))
last=d1.popitem()
last_val=last[-1]
print("Last val: ", last_val)
