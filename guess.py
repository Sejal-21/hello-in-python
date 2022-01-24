import random
b= random.randint(1,9)
# print(b)
a= input("guess a number between 1 to 9")
a= int(a)
if a==b:
    print("your guess number is right",a ,b)
else:
    print("your guess number is wrong",a ,b)



