#To print prime number in the interval of user input : a and b. 

upper = int(input("Enter upper value : "))
lower = int(input (" Enter lower value : "))
#Prime number is divisible by number 1 and itself
for num in range(lower,upper + 1):  
    if num>1:
        for n in range(2,num):
            if (num%n)==0:
               break
        else:
                    print (num)

