s="PYTHON"
print("BY Using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")#My req todays is display pyth without using indexing and sclicing
    print("---------------------------------------------")
    for ch in s: #s="python"
     if(ch=="N"):
         break
     print("{}".format(ch),end="")
    else:
            print("I am from else part of for loop")
            print("\nOther Statements in program")