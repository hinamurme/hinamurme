n=int(input("Enter the num:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("_"*50)
    print("natural number\t\t square\t\tcubes")
    print("_"*50)
    s,ss,sc=0,0,0
    for i in range(1,n+1,):
        print("\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        print("_"*50)
        sc=sc+i**3
        print("\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format(s,ss,sc))
        print("_"*50)