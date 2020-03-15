my_str=input('please inoput a string:\n')
digit_str='0123456789'
flag=False
for c in my_str:
    if c not in digit_str:
        flag=True
if flag:
    print('NOT all numbers')
else:
    print('all numbers')