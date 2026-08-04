# def n():    
#     n=int(input("enter the n--"))
#     return n

# def n_natural(n):
#     if n<1:
#         return       
#     n_natural(n-1)
#     print(n)
        

# n_natural(10)

# def n():
#     int(input("Enter the value"))
#     return n

# def recursive_sum(n):
#     if n>1:
#         return 
#     recursive_sum(n-1)
#     print(n)

# recursive_sum(10)

# def n():
#   n=int(input("Enter the value"))
#   return n

# def recursive_even_series(n):
#     if n>1:
#         return 
#     if(n%2==0):
#         recursive_even_series(n-1)
#         print(n)


# def multiplication(n,i=10):
#   if i==0:
#     return
#   multiplication(n,i-1)
#   print(n*i)


# multiplication(5)

# Factorial
# def fact(n):
#   if n==0 or n==1:
#     return 1
#   return n* fact(n-1)

# print(fact(5))

# Sum of n natural

# def sum(n):
#   if n==0:
#     return 0

#   return n+sum(n-1)

# print(sum(5))

# def print_digit(n):
#   if n<=0:
#     return 
#   print_digit(n//10)
#   print(n%10)
# print_digit(101)

# print only odd digits
# def print_digit(n):
#   if n<=0:
#     return 
#   print_digit(n//10)
#   if n%2!=0:
#    print(n%10)
# print_digit(101)

# Print only even digits
# def print_digit(n):
#   if n<=0:
#     return 
#   print_digit(n//10)
#   if n%2==0:
#    print(n%10)
# print_digit(101)
  
# Print only zeros of a number
# def print_digit(n):
#   if n<=0:
#     return 
#   print_digit(n//10)
#   if n==0:
#    print(n%10)
# print_digit(101)


# def print_digit(n):
#   if n<=0:
#     return 
#   print_digit(n//10)
#   if n%2!=0:
#    print(n%10)
# print_digit(101)

# def prime_or_not(n,i=2,is_prime=True):
#   if i==n:
#     return is_prime
#   if n%2==0:
#     is_prime=False
#     return prime_or_not(n,i,is_prime)
#   else:
#     i=i+1
#     return prime_or_not(n,i,is_prime)

# print(prime_or_not(9))

# def print_numbers(lrange,urange):
#     # Base case
#     if lrange>urange:
#       return

#     print(lrange) 

#     print_numbers(lrange+1,urange)
    

# print_numbers(1,20)


# def print_numbers(lrange,urange):
#     # Base case
#     if lrange>urange:
#       return
    
#     if lrange%2==0:

#       print(lrange) 

#     print_numbers(lrange+1,urange)
    

# print_numbers(1,20)

# def print_num(n):
#     if n==0:
#         return 
#     print_num(n-1)
#     print(n)

# print_num(10)

# print n natural odd numbers
# def print_odd(n):
#     if n==0:
#         return
#     print_odd(n-1)

#     if n%2!=0:
#         print(n)   

# print_odd(20)

# printing natural palindrome numbers in reverse order

# def palindrome(n):
#     original =n
#     reverse=0
#     while(n!=0):
#         digit=n%10
#         reverse=reverse*10+digit
#         n//=10

#     if original==reverse:
#         return True
  
# def print_palindrome(n):
#     if n==0:
#         return
#     if palindrome(n)==True:
#         print(n)

#     print_palindrome(n-1)
    
# print_palindrome(200)

# making table using recursion

# def multiplication_table(n, i=10):
#     if i==0:
#       return
    
#     multiplication_table(n,i-1)
#     print(n,'x',i,'=',n*i)

# multiplication_table(2)
    
# print digits of a number

# def print_digit(n):
#     if n==0:
#         return
#     removed=n//10
#     print_digit(removed)
#     digit=n%10
      # if n%2==0:
#     print(digit)


# Print odd digit of a number
# num=int(input("enter the values--"))
# print_digit(num)

# def print_digit(n):
#     if n==0:
#         return
#     removed=n//10
#     print_digit(removed)
#     digit=n%10

#     if n%2!=0:
#      print(digit)

# num=int(input("enter the values--"))
# print_digit(num)


# Print even digits of a number
# def print_digit(n):
#     if n==0:
#         return
#     removed=n//10
#     print_digit(removed)
#     digit=n%10

#     if n%2==0:
#      print(digit)

# num=int(input("enter the values--"))
# print_digit(num)

# def print_digit(n):
#     if n==0:
#         return
#     removed=n//10
#     print_digit(removed)
#     digit=n%10

#     if n%5==0:
#      print(digit)

# num=int(input("enter the values--"))
# print_digit(num)

# reversing an number using recursion
# def reverse_number(n):
#     # base case
#   if n==0:
#     return
  
#   rev=0
#   digit=n%10
#   rev=rev*10+digit

#   print(rev)
#   reverse_number(n//10)

# reverse_number(1234)

# Sum of n natural numbers
# def sum(n):
#   if n==0:
#     return 0
#   total=n+sum(n-1)
#   return total

# print(sum(5))

# def factorial(n):
#     if n==0 or n==1:
#         return 1
    
#     fact=n* factorial(n-1)
#     return fact
# print(factorial(5))


# def sum_digit(n):
#     if n==0:
#         return 0 
    
#     return (n%10)+sum_digit(n//10)
# print(sum_digit(121))

