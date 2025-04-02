n= int(input("Enter the Any number:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("_"*50)
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    else:
        print("{}!={}".format(n,fact))
        print("_"*50)