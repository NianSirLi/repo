#2020.1.24 python study class 1

#0 键盘输入
a=input("please input a digit:\n") #执行该语句时会先在终端显示这句话，再等待键盘输入一个值赋给a
#print末尾自带换行
a+a#input输入的默认为字符串，可以直接相“加”

#1 并行赋值（同时对多个变量赋值）
x,y,z=1,2,3
#交换变量值变得极其方便
x,y=y,x

#2 python动态数据类型，查看数据类型，查看地址
x=1
type(x)
id(x)
x="word"
id(x)#id变化，说明并不是x原地址的内容发生变化，而是x重新指向了存储在另一内存空间的另一个对象

#3 复数类型
z=1+3j
z=complex(1,100)
z.real
z.imag
z.conjugate()#求共轭

#4 除法与整除的不同
3/2#除法，默认浮点型
3//2#整除。默认取不完全商

#5 允许使用级联比较形式
a,b,c=1,2,3
a<b<c
a<b>c

#6 浮点数据的判断相等操作
#不能使用==判断浮点数据的相等
2.1-2.0==0.1
#通常选的误差为10的-9次方
esp=0.000000001
#应使用判断二者的误差是否足够小来判断二者是否相等
abs((2.1-2.0)-0.1)<esp

#7 python的逻辑运算符是单词and，or，not

#8 python的非内置模块
help('math')#查看非内置模块math的内容

#9 python的非内置模块
#导入非内置模块函数的第一种办法-较繁但可避免重名
import math
math.pow(math.pi,2)#幂函数
round(math.pi,1)#保留一位小数
#导入非内置模块函数的第二种办法-写法简单
from math import *
#所有的math.都可以去掉，但要保证同一程序中没有来自两个包的两个相同的函数名

'''
python中的容器类型分为：
   1序列：字符串、元组、列表（元组被赋值后不能被修改）
   2无序的数据集合体：集合、字典
'''
#10 批量数据类型的基本操作
#前4个操作为序列特有，以字符串为例
#(1)联接
'he'+'llo'
#(2)复制n次
'hi '*5
#(3)下标操作
'python'[0]
'python'[-1]#下标负数，意为倒数第几个
#(4)引用序列中的子序列
'hello python!'[2:8:2]#从begin到end-1，间隔切片（最小为1）
#(5)计算序列中成员的个数
len('hi ')
#(6)检测某子序列是否在序列中
'n!' not in 'hello python!'
#(7)计算序列中的最大项，最小项，以元组为例
max((1,2,3))
min((1,2,3))
#(8)类型构造器：无参数时生成空的对象，有参数时将一个其他对象转换为本类对象。
a=list()
a=list('python')
a

#11 文本信息处理-python的字符串类型
#创建元组
t=1,2,3
t=(1,2,3)
t=()
t

#12 列表
#列表的字面表示
L=['one','two','three','four','five']
L=[]
L=list(('he','her','here'))#类型构造器
L
#列表元素的修改
L8=[[1,2],[3,4],[5,6]]
L8[2]=5#修改第三项
L8
L8[0][0]=10#修改第一项（还是列表）的第一项
L8

#列表对象方法
t=[]
t.append(1)#末尾加一个数
t.extend([2,3,4])#末尾加一系列数
t
t.remove(2)#去掉2
t.insert(3,5)#在第三个位置插入5

#列表元素排序
t=[2,1,3,4]
t.sort()
t
t.sort(reverse=True)

#13 集合
s={1,2,3,4,5}
s=set('hello')
s
#列表去重复操作实例
L={1,2,3,4,1,2,3,4}
L=list(set(L))
#循环遍历访问集合元素
s={1,2,3,4}
for i in s:
    print(i,end=' ')#print末尾默认为回车，此处改为空格
#集合对象的常用方法
s={1,2}
s.add(3)
s.remove(3)
s.clear()

#14 字典
#字典的创建
d={'JAN':31,'FEB':28}
d=dict(JAN=31,FEB=28)
#字典元素的访问与修改
d['FEB']=29
#字典元素的增删
d["test"]=1
del d['test']
#字典对象的方法
d={1:'MON',2:'TUE'}
d.keys()
d.values()
d.items()
d.pop(1)
d.get(2)
d.get(1,"!")

d={1:'MON',2:'TUE'}
monthdays=dict(JAN=31,FEB=28)
d.update(monthdays)
d.clear()
#字典元素键值的遍历
monthdays=dict(JAN=31,FEB=28)
for i in monthdays.keys():
    print(monthdays[i],end=' ')
#字典元素的排序法一
scores={3:'li3',1:'wang1',2:'zhang2'}
L1=list(scores.keys())
L1.sort()
#法二
L2=[]
for i in range(0,len(L1)):
    L2.append(scores[L1[i]])
L2