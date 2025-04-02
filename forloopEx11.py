line=input("Enter the line of text:")
print("\n{} Given line".format(line))
words=line.split()
print("Given line into words")
for word in words:
    print("\t{}--->{}".format(word,len(word)))

