line=input("Enter the text:")
lc=""
for ch in line:
    if (ord(ch)) in range(97,123):
        lc=lc+chr(ord(ch)-32)
        if(ord(ch) in range(65,91)):
         lc=lc+ch
         if (ord(ch) in range(32,65)):
             lc=lc+ch
else:
            print("Given Line=",line)
            print("upper case data=",lc)



