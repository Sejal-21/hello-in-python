b= input("Enter first number:")
b= int(b)
c= input("Enter second number:")
c= int (c)
print("What operation do you want to perform\n")
print(" 1. Addtion \n 2. Subtraction \n 3. Division \n 4. Multiplication \n 5. Modulus \n ")
a= input("Enter your choice:")
a= int(a)
if a==1:
    print("Addtion is :", b+c)
elif a==2:
    print("Subtraction is :", b-c)
elif a==3:
    print("Division is :", b/c)
elif a==4:
    print("Multiplication is :", b*c)
elif a==5:
    print("Modulus is :", b%c)
else:
    print("Wrong choice")

