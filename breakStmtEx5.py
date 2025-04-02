n=int(input("Enter the Any number:"))
if(n<=1):
    print("{} is invalid".format(n))
else:
    print("-"*50)
    res="prime"
    for i in range(2,n):
        if n%i==0:
         res="not prime"
        break
    print("{} is {}".format(n,res))