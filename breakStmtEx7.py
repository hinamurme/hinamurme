s=input("Enter a word/line of text:")
d=dict()
for ch  in s:
    if ch not in d:
      d[ch]=1
    else:
      d[ch]=d[ch]+1
else:
    for k,v in d.items():
        print("{} -->{}".format(k,v))


