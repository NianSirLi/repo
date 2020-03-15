print('input 1 to convert Fahrenheit to Celsius')
print('input 2 to convert Celsius to Fahrenheit')
opt=input('please input 1 or 2:')
if opt!='1' and opt!= '2':
    print('input error')
elif opt=='1':
    d=input('please input Fahrenheit temperature:')
    t=float(d)
    if (t<=-459.67):
        print('input error')
    else:
        print('converted Celsius temperature is:')
        print(round((t-32)/1.8,2))
elif opt=='2':
    d=input('please input Celsius temperature:')
    t=float(d)
    if t<=-273.15:
        print('input error')
    else:
        print('converted Fahrenheit temperature is:')
        print(round((t*1.8)+32,2))
        

