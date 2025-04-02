n=int(input("enter how many natural num u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("_"*50)
    print("natural num within:{}".format(n))
    print("_"*50)
    ps=1
    for i  in range(1,n+1):
        print("\t{}".format(i))
        ps=ps+i
    else:
        print("*"*50)
        print("product={}".format(ps))
        print("_"*50)