n = int(input('enter the number:'))
s = 0 
while n != 0 :
    r = n % 10
    s = s*10 + r
    n = n//10
print('palindrome = ',s,end = ' ')
    