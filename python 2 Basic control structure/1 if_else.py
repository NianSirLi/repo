d=input('please input the temperature in Fahrenheit:')
f=float(d)
if f <= -459.67:
    print('input error')
else:
    print('the temperature in Celsius is:') 
    print(round((f-32)/1.8,2))

