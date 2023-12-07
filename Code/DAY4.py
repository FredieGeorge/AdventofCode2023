f=open('DAY4','r')
a=f.readlines()
get_=[1]*219
summer=0
for num,i in enumerate(a):
    i=i.split(':')[1]
    b,c=i.split('|')
    b=b.split(' ')
    c=c.split(' ')
    b_new=[]
    c_new=[]
    for i in b :
        if i!='':
            b_new.append(int(i))
    for i in c:
        if i!='':
            c_new.append(int(i))   
    b,c=b_new,c_new
    index=0
    for j in c_new:
        if j in b_new:
            index+=1
    if index!=0:
        for loo in range(num+1,num+index+1):
            get_[loo]+=get_[num]
print(sum(get_))