# n= int(input("Enter the value--"))
# i=1
# while(i<=n):
#     print(i)
#     i+=1

# n=int(input("enter the number--"))
# while(n>=1):
#  print(n)
#  n-=1

# n= int(input("Enter the number --"))

# i=1

# while(i<=10):
#     print(n*i)
#     i+=1

# n=int(input("Enter the value"))

# i=1
# while(i<=n):
#     if(i%2!=0):
#         print(i)
#     i+=1

# n= int(input("Enter the number--"))

# i=1
# while(i<=n):
#     if(i%5==0):
#         print(i)
#     i+=1

# num=int(input("Enter the value--"))
# sum=0
# i=1
# while(i<=num):
#     sum=sum+i
#     i+=1

# print(sum)

num=428
while num>0:
    last_digit=num%10
    # print(last_digit)
    num//=10


reverse=str (num[::-1])
print(reverse)




