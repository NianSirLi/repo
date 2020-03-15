#约瑟夫环问题的python实现
mylist=range(1,31)
delete_list=[] 
x=0 #x表示人的遍号
i=0 #i表示报的数
while len(delete_list)<15:#只求出列的前15个人的号码
    if(x>29):
        x=0 #x=30和x=0是一样的
    if(mylist[x] not in delete_list):#如果人不在已经出列的人的列表中，报数就+1（已出列的话就没有任何操作，相当于跳过它）
        i+=1 
    if i==9:#报到9时，进入环节：处理出列和清0
        print(mylist[x])
        print('List out')
        delete_list.append(mylist[x])#将已出列的人加入delete_list中
        i=0 #后一个人重新开始报数
    x+=1 #x不断循环，不断转圈到不同的人