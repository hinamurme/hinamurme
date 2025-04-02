print("*"*50)
n=int(input("Enter the Any number:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("*"*50)
    i=n
    while(n>=2):
        print(n)
        n-=2