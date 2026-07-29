# functions without args and without return types
# def oddEven():
#     num=int(input("Enter the number--"))
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")

# oddEven()

# check palindrome or not

# def checkPalindrome(num):
#     original=num
#     reverse=0
#     while(num!=0):
#         digit=num%10
#         reverse=reverse*10+digit
#         num=num//10
#     if original==reverse:
#         print(original,"-> Palindrome")
#     else:
#         print(original,"-> NOt palindrome")

# checkPalindrome()

# def printName(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# printName(10,20,30)

# def checkOdd(a):
#     if a&1==0:
#         print(a,"->Even")
#     else:
#         print(a,"->Odd")

# # checkOdd(9)

# l1=[10,20,33]

# for i in l1:
#     checkOdd(i)

# l1=[10,20,33]

# for i in l1:
#     checkPalindrome(i)

# def square():
#     num=int(input("Enter the number--"))
#     sqr=num**2
#     return sqr

# print(square())


# return keyword example
# def demo():
#     return 10

# var=demo()
# print(var)

# def getSquare(num):
#     return num*num

# var=getSquare(5)
# print(var)

# def getReverse(num):
#     reverse=0
#     while num!=0:
#            digit=num%10
#            reverse=reverse*10+digit
#            num=num//10
   
#     return reverse 

# var=getReverse(123)
# print(var)

# def add(a,b,c):
#     res=a+b+c
#     return res

# var=add(10,20,30)
# print(var)

# def checkOdd(num):
#     if num & 1==0:
#         return False
#     else:
#         return True
    
# num=int(input("Enter the value--")) 
# var=checkOdd(num)
# print(var)

# def is_palindrome(num):
#     original=num
#     reverse=0

#     while(num!=0):
#         digit=num%10
#         reverse=reverse*10+digit
#         num//=10

#     if original==reverse:
#         return True
#     else:
#        return False

# num=int(input("Enter the value--"))
# var=is_palindrome(num)
# print(var)

# def is_int(num):
#     val=num
#     if val.isdigit():
#         return True
#     else:
#         return False
    
# num=input("Enter the value--")
# var=is_int(num)
# print(var)

# def is_two_digit(num):
#     if num>9 and num<100:
#         return True
#     else:
#         return False
    
# num=int(input("Enter the value--"))
# var=is_two_digit(num)
# print(var)

# def multiple_of_five(num):
#     if num%5==0:
#         return True
#     else:
#         False

# num=int(input("Enter the value--"))
# var=multiple_of_five(num)
# print(var)

# def is_prime(num):
#     count=0
#     i=1
#     while(i<=num):
#         if num%i==0:
#             count+=1
#         i+=1

#     if count>2:
#         return False
#     else:
#         return True
    
# num=int(input("Enter the value--"))
# var=is_prime(num)
# print(var)

# def add_digits(num):
#     sum=0
#     i=1
#     while(i<=num):
#         sum=sum+i
#         i+=1

#     return sum

# num=int(input("Enter the value--"))
# var=add_digits(num)
# print(var)

# def product_digits(num):
#     product=1
#     i=1
#     while(i<=num):
#         product=product*i
#         i+=1

#     return product

# num=int(input("Enter the value--"))
# var=product_digits(num)
# print(var)

# Store the factorial od numbers in a list



# list1=['hii',2,8.99,'bye',5,4,"Python"]
# list2=[]
# def is_factorial(num):

#     for i in list1:
#         if type(i)==int:
#            val= factorial()
#         list2.append(val)
            

# print(list2)

# def is_prime(num):
#     count=0
#     i=1
#     while(i<=num):
#         if num%i==0:
#             count+=1
#         i+=1

#     if count==2:
#         print("Prime")
#     else:
#         print("Not prime")

# is_prime(11)

# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n % i==0:
#             return False
#     return True

# def prime_series(n):
#     li=[]
#     for i in range(1,n+1):
#         if is_prime(i):
#             li.append(i)
#     return li

# def prime_of_prime(n):
#     li=prime_series(n)
#     for i in li:
# def series_prime(n):
#     count=0
#     for i in range(1,n+1):
#         for j in range(i,n+1):
#             if n % j==0:
#                 count+=1
#         if count==2:
#          print(i)


# var=series_prime(11)
# print(var)

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*num

#     return fact

# var=factorial(10)
# print(var)
    
# def strong(n):
#     original=n
#     sum=0
#     for i in range(1,n+1):
#         for j in range(i,n+1):
#             if factorial(n):
#                 sum+=j
#     if original==sum:
#         print("Strong")
#     else:
#         print("Not Strong")
    
#     strong(14)

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i

#     return fact

# # var=factorial(5)
# # print(var)

# def is_strong(n):
#     sum=0
#     for i in str(n):
#         sum=sum+ factorial(int(i))

#     if n==sum:
#         return True
#     else:
#         return False
    
# print(is_strong(145))

# def is_prime(n):
#     count=0
#     i=1
#     while(i<=n):
#        if n%i==0:
#           count+=1
#        i+=1

#     return count==2

# def prime_series(n):
#     for i in range(1,n+1):
#      if is_prime(i):
#        print(i)
       

# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def prime_of_prime(n):
#     for num in range(2, n + 1):
#         if is_prime(num):
#             digit_sum = 0
#             temp = num

#             while temp > 0:
#                 digit_sum += temp % 10
#                 temp //= 10

#             if is_prime(digit_sum):
#                 print(num)


# n = int(input("Enter range: "))
# prime_of_prime(n)


# xylem or phloem

# def is_xylem(n):
#     last_digit=n%10
#     print(last_digit)
#     temp=n
#     while temp>=10:
#         temp//=10
#     first_digit=temp
#     print(first_digit)

#     extreme_sum=first_digit+last_digit
#     print(extreme_sum)

#     total_sum=0
#     temp=n

#     while temp>0:
#      last=temp %10
#      total_sum= total_sum+last
#      temp//=10

#     mean_sum=total_sum-extreme_sum

#     if extreme_sum==mean_sum:
#        print("Xylem")
#     else:
#        print("Phloem")

# is_xylem(12326)

def is_xylem(n):
    last_digit=n%10
    temp=n

    while temp>10:
        temp //=10
    first_digit=temp
    print(first_digit)

    extreme_sum=first_digit+last_digit

    sum=0
    temp=n

    while temp>0:
        digit=temp%10
        sum=sum+digit
        temp//=10

    mean_sum=sum-extreme_sum

    if extreme_sum==mean_sum:
        print("Xylem")
    else:
        print("Pholem")

is_xylem(1234)










        



    



