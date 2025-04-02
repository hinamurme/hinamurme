n=int(input("Enter Any number:"))
if(n<=0):
    print("{} is invalid input".format(n))
    print("*"*50)
fact=1
for i in range(1,n+1,1):
        fact=fact*i
else:
    print("_"*50)
print("{} != {} factorial".format(fact,n))
print("_"*50)