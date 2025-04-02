#Program for Demonstrating the Need of break Keyword
#BreakStmtEx3.py
s="kkiki"
for ch in s:
    print("\t{}".format(ch),end='')
else:
    print("---------------------------------------")
#My Req is to display  MISS without using Indexing and Slicing
ictr=0
for ch in s: # s="MISSISSIPPI"+-
    if ch =="k":
     ictr+=1
     if ictr==3:
      break
    print("{}".format(ch),end="")
else:
    print("---------------------------------------")
print()
print("********************************************")