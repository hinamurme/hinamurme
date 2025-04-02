num=int(input("Enter the number if you want:"))
if(num<=0):
    print(" {} is invalid".format(num))
else:
    lst=list()
    for i in range(1,num+1):
        val=input("\t Enter {} word:".format(i))
        lst.append(val)
    else:
        print("list of words")
        print(lst)