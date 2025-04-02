n=int(input("Enter the Any number:"))
if(n<=0):
    print("{} lis invalid".format(n))
else:
  res=True
for i in range(2,n):
     if n%i==0:
      res=False
     break
res="prime" if res else "not prime"
print("{} is {}".format(n,res))
