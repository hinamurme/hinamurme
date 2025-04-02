s="PYTHON"
print("BY Using while loop")
i=0
while(i<len(s)):
 print(s[i])
 i=i+1
else:
 print("I am from else part of while loop")#Req today is to display pyth without using indexing and slicing
 print("-------------------------------------------------")
 i=0
while(i<len(s)):#s="python"
    if(s[i]=="O"):
        break
    print("{}".format(s[i],end=""))
    i=i+1
else:
    print("I am from else part of while loop")
    print("\n Other statement in program")

