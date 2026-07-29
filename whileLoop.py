# Printing 1 to n
# n=int(input("Enter the number--"))

# i=1

# while(i<=n):
#     print(i)
#     i+=1

# Printing n natural numbers inverse order
# n=int(input("Enter the number--"))
# while(n>=1):
#     print(n)
#     n-=1

# wap to print n natural numbers in a given range(n1 to n2)
# n1=int(input("Enter the n1--"))
# n2=int(input("Enter the n2--"))

# while(n1<=n2):
#     print(n1)
#     n1+=1

# Printing Multiplication table
# n=int(input("Enter the number for the table--"))

# i=1
# while(i<=10):
#     print(n,'x',i,'=',n*i)
#     i+=1

# Printing n even numbers

# n=int(input("Enter the range--"))

# i=1

# while(i<=n):
#     if(i%2==0):
#         print(i)
#     i+=1

# Printing n odd numbers

# n=int(input("Enter the range--"))

# i=1

# while(i<=n):
#     if(i%2!=0):
#         print(i)
#     i+=1

# Printing n natural number divisible by 5
# n=int(input("Enter the range--"))

# i=1

# while(i<=n):
#     if(i%5==0):
#         print(i)
#     i+=1

# Printing n natural palindrome
# n=int(input("Enter the number--"))
# original=n
# reverse=0

# while(n>0):
#     last_digit=n%10
#     reverse=reverse*10+last_digit
#     n=n//10

# if(original==reverse):
#     print("Yes! Its a palindrome")
# else:
#     print("Oops! Not a palindrome")

# Printing n natural palindrome
# n=int(input("Enter the number--"))

# i=1

# while(i<=n):
    
#     if str(i)==str(i)[::-1]:
#         print(i)
    
#     i+=1

# Printing sum of n natural numbers
# n=int(input("Enter the number--"))
# sum=0
# i=1

# while(i<=n):
#     sum=sum+i
#     i+=1

# print(sum)

# Printing product of n natural number

# n=int(input("Enter the range--"))

# i=1

# product=1

# while(i<=n):
#     product=product*i
#     i+=1
# print(product)

# Printing factorial of a given number
# n=int(input("Enter the number--"))
# fact=1
# while(1<=n):
#     fact=fact*n
#     n-=1
# print(fact)

# wap to print digit of a number and digits who are even
# num=int(input("Enter the number"))

# while(num>0):
#     digit=num%10
#     if digit%2==0:
#         print(digit)
#     num=num//10

# wap to count no of zeros from a number
# num=int(input("Enter the number--"))
# count=0
# while(num>0):
#     digit=num%10
#     if digit==0:
#         count+=1
#     num=num//10

# print("No of zeros are:",count)

# num=int(input("Enter the number--"))

# sum=0

# while(num>0):
#     digit=num%10
#     sum=sum+digit
#     num=num//10

# print(sum)

# num=int(input("Enter the number--"))

# product=1

# while(num>0):
#     digit=num%10
#     product=product*digit
#     num=num//10

# print(product)

# Palindrome
# num=int(input("Enter the number--"))
# original=num
# reversed=0
# while(num>0):
#     digit=num%10
#     reversed=reversed*10+digit
#     num=num//10

# if reversed==original:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# num=int(input("Enter the number--"))

# i=1

# while(i<=num):
#     if num%i==0:
#         print(i)
#     i+=1

# num=int(input("Enter the number--"))
# i=1
# count=0
# while(i<=num):
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print('prime')
# else:
#     print('not prime')

# perfect number
# num=int(input("Enter the number--"))
# sum=0
# i=1
# while(i<num):
#     if num%i==0:
#         sum=sum+i
#     i+=1
# if num==sum:
#     print("perfect number")

# num=int(input("Enter the number--"))
# original=num
# sum=0

# while(num>0):
#     digit=num%10
#     cube=digit**3
#     sum=sum+cube
#     num=num//10
# print(sum)

# if original==sum:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")


#num=int(input("Enter the number--"))

# count=0
# i=1

# while(i<=num):
#     if num%i==0:
#         count+=1
#     i+=1

# if count==2:
#     print("Prime number")
# else:
#     print("not a prime number")

# num=int(input("enter the number--"))

# i=1

# original=num
# sum=0

# while(num>0):
#     digit= num%10
#     cube=digit**3
#     sum=sum+cube
#     num=num//10
# i+=1

# if original==sum:
#     print("Its a armstrong number")
# else:
#     print("Its not a armstrong number")

# num=int(input("Enter the number--"))

# sum=0
# i=1
# while(i<num): 
#    if num%i==0:
#       sum=sum+i
#    i+=1
   
# if sum ==num:
#    print("Perfect number")

# else:
#    print("not perfact number")



#xylem and pheloem no.

# num=int(input('enter no.'))
# last=num%10
# num=num//10
# first=num//(10**((len(str(num))-1)))
# mean=0
# while num>0:
#     if num%10!=first:
#         mean+=num%10
#     num//=10
# if first+last==mean:
#     print('xylem')
# else:
#     print('pheloem')


# spy number
# num=int(input("Enter the number--"))
# original=num
# product= 1
# sum=0

# i=1
# while(i<=num):
#     digit=num%10
#     product=product*digit
#     sum=sum+digit
#     num//=10

# i+=1

# if product==sum:
#     print("Spy number")
# else:
#     print("Not spy")
    
# Disarium number
# num=input("Enter the num--")
# sum=0
# position=1
# for i in num:
#     sum=sum+ int (i)**position
#     position+=1

# print(sum)

# if sum==int (num):
#     print("Dissarium number")
# else:
#     print("Not an disarium number")
    
# num=int(input("Enter the number--"))

# i=1

# count=0

# while(i<=num):
#     if num%i==0:
#         count+=1
#     i+=1

# if count==2:
#     print("prime number")
# else:
#     print("Not prime number")
   
# xylem or phloem number


# num=int(input("Enter the number--"))

# temp=num

# last_digit=temp%10

# while temp>10:
#     temp //=10
# first_digit=temp

# extreme_sum=first_digit+last_digit

# temp2=num

# total=0
# while(temp2>0):
#     digit= temp2%10
#     total=total+digit
#     temp2//=10

# mean_sum=total-extreme_sum

# if extreme_sum==mean_sum:
#     print("Xylem")
# else:
#     print("Phloem")
    
# def person(name,age,email="NA"):
#     print(name)
#     print(age)
#     print(email)

# person("Ankit",21,"ankit@gmail.com")
# person("Rakesh",30)

def demo(*args):
    print(args,type(args))
demo(10,20,30,40,50)














