# Program to find LCM of two numbers
Num1=int(input("Enter the first number:"))
Num2=int(input("Enter the second number:"))
# LCM is the smallest multiple of two numbers
if(Num1>Num2):
    min1=Num1
else:
    min1=Num2
while(1):
    if(min1%Num1==0 and min1%Num2==0):
        print("LCM is:",min1)
        break
    min1=min1+1
