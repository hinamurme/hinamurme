line=input("Enter a line of text:")
print("Given line={}".format(line))
words=line.split()
print("given line into words")
for word in words[::-1]:
    print("\t{}".format(word))