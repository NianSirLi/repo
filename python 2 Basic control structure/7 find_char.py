#find whether there is 'a' in entered string
while 1:
    str=input('please input a str (input "quit" to quit):\n')
    if(str=='quit'):
        break
    else:
        if str.count('a')!=0:
            print('find "a" !')
        else:
            print('NOT find "a" !') 