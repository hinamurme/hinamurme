line=input("Enter line of text:")
lc=" "
for ch in range(len(line)-1,-1,-1):
    if (ord(line[ch]) in range (65,91)):
         lc=lc+chr(ord(line[ch])+32)
    if(ord(line[ch]) in range (97,123)):
     lc=lc+line[ch]
    if(ord(line[ch])in range(32,65)):
          lc=lc+line[ch]
    else:
      print(lc)