line=input("Enter line of text:")#line=python
rs=""
for i in range(len(line)-1,-1,-1):
    rs=rs+line[i]
else:
    print("given string={}".format(line))
    print("reverse string={}".format(rs))