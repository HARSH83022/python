num = int(input('enter the number'))
cp=num
s=0
while num !=0:
    r= num %10
    s=s*10 +r
    num = num //10

if s==cp:
    print('palindrome number')
else:
    print('not a palindrome number')
    
