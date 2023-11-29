# password validation
#self doing

import time
password = 'harsh12!0'

while 1:
     user_pass = input('enter the password')
     if user_pass == password:
         print('login succesfull')
         break
else:
    print('worng password,try again')
attempt= 3
attempt -= 1
if attempt <=0:
    print('failed to login ')
    print('waiting TIme start')
    count=10
    while count:
        time.sleep(1)
        print(count,end='')
        count-=1
        attempt =3 
    
