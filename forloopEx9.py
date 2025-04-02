line=input("Enter the line of text:")
print("given line\n{}".format(line))
words=line.split()
for index in range(len(words)):
 words[index]=words[index][::-1]
print(" ".join(words))