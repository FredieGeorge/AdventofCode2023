f=open("DAY15","r")
list=[[] for i in range(256)]
def hash(a):
    value=0
    for i in a:
        value+=ord(i)
        value*=17
        value%=256
    return value
a=f.read()
a=a.split(',')
for i in a:
    if '=' in i:
        temp=i.split('=')
        label=hash(temp[0])
        in_it=True
        for i in list[label]:
            if i[0]==temp[0]:
                i[1]=temp[1]
                in_it=False
                break
        if in_it:
            list[label].append([temp[0],temp[1]])
    elif '-' in i:
        label=hash(i[:-1])
        for j in list[label]:
            if j[0]==i[:-1]:
                list[label].remove(j)
                break
print(list)
sum=0
for i in range(len(list)):
    for ii in range(len(list[i])):
        sum+=(i+1)*(ii+1)*int(list[i][ii][1])
print(sum)