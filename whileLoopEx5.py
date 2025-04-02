line=input("enter any char:")
print("*"*50)
print("given line={}".format(line))
print("w.r.t while loop in forward direction with +ve index")
print("*"*50)
i=0
while(i<len(line)):
    print("\t\t {}-->{} ".format(i,(line[i])))
    i+=1
    print("*"*50)
    print("w.r.t")
else:
    print("*"*50)
    i=0
    while(i<-len(line)):
        print("\t\t {}-->{}".fromat(line[i]))