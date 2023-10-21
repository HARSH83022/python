from time import*
passwrd = 'mfwqingbish'
c = 3
while 1 :
    user_pass= input('ENTER THE PASSWORD')
    if user_pass==passwrd:
        print('login successful')
        break  
    else :
        print('Wrong password')

    c-=1
    if c<=0:
        print('login failed')
        print('waiting time start')
        count = 6
        while count:
            sleep(2)
            print(count,end=' ')
            count-=1

       