line=input("Enter the line of text:")
lst=list()
for ch in line:
    if ch not in lst:
      lst.append(ch)
else:
       print("Given line",line)
       print("Unique values=","".join(lst))