a = input("ENTER THE WORD==")
ch = ""
for i in a :
   if a.count(i)>=2 and i not in ch:
      ch +=i
print(ch)