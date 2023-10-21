num = int (input('enter the number'))
cp = num
pw = 0 
while num !=0 :
    num = num//10
    pw += 1
num = cp
s = 0
while num !=0:
    r = num% 10
    s = s+r**pw
    num = num //10
print('ARMSTRONG NUMBER ' if cp ==s else 'NOT A ARMSTRONG' )