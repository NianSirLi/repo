deposit=10000
years=0
r0=input('please input annual interest rate:')
r=float(r0)
while deposit<20000:
    years+=1
    deposit=deposit*(1+r)
print(str(years)+' years later deposit will double')