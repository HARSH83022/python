#multilication table of given number

num=int(input('enter the number'))
i=1

while  i <=10:
    print(f'{num:<3} X {i:>2} = {num*i:>4}')
    i +=1
