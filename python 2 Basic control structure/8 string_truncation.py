while 1:
    mystr=input('please input a product coding (input "quit" to quit):\n')
    if(mystr=='quit'):
        break
    else:
        if mystr[0]=='1':
            print('Commodity in the market,')
        else:
            print('Commodity delisting,')
        
        year=mystr[2:6]+','
        month=mystr[6:8]+','
        day=mystr[8:10]+','
        print('The delivery date of the goods is ' + year + month + day)