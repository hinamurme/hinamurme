s=input("Enter the num/char:")
for ch in s:
    print("\t{}".format(ch))
else:
    print("------------------------------------------")
    #My Req is to display MISS without using Indexing and slicing
    itr=0
    for ch in s:#s="MISSISSIPPI"
     if(ch=="I"):
       itr +=1
     if(itr==2):
       break
       print("{}".format(ch),end=" ")
     else:
      print("----------------------------------------")
    print()
    print("----------------------------------------")

