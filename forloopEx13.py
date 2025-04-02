nov=int(input("Enter How many value u want to enter:"))
if(nov<=0):
    print("{} is invalid input".format(nov))
else:
    lst=list()
    for i in range(1,nov+1):
        val=float(input("Enter {} value:".format(i)))
        lst.append(val)
    else:
        print("list of value")
        print(lst)