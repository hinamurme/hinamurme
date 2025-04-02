print("*"*60)
n=int(input("Enter the number:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("*"*50)
    i=n
    while(n>=1):
        print(n)
        n-=2