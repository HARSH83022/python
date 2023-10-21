from random import*
attempt1=5
attempt2=5
c_num = randrange(1,51)
while 1:
    u_num1 = int(input('USER1 GUESS THE NUMBER:'))
    if u_num1==c_num:
        print('USER1 WINN!!','WITH attempt ',attempt1)
        break
    elif u_num1>c_num:
        print('TOO LARGE -_-','attempt left ',attempt1)
    elif u_num1<c_num:
        print('TOO SMALL -_-','attempt left ',attempt1)
    if attempt1==0:
        print('you both lose')
        break
    attempt1-=1
    u_num2= int(input('USER2 GUESS THE NUMBER:'))
    if u_num2==c_num:
        print('USER2 WINN!!','WITH attempt ',attempt2)
        break
    elif u_num2>c_num:
        print('TOO LARGE -_-','attempt left ',attempt2)
    elif u_num2<c_num:
        print('TOO SMALL -_-','attempt left ',attempt2)
    if attempt2==0:
        print('you both lose')
        break
    attempt2-=1

        
    

        

    