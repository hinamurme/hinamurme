print("*" * 50)
n=int(input("Enter the Any number:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("*"*50)
    print("{} mul with this num".format(n))
    i=10
    while(1<=i):
        print(i,"*",n,"=",i*n)
        i-=1