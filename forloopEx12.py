line=input("Enter the line of text:")
print("Given line={}".format(line))
words=line.split()
print("Given line into word")
d={ }
for word in words:
    d[word]= len(word)
else:
 for w,wl in d.items():
     print("\t{}--->{}".format(w,wl))