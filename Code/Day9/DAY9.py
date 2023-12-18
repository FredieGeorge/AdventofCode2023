f=open("DAY9","r")
sum_=0
c=f.readlines()
def successive_difference(a):
    temp=[]
    for i in range(1,len(a)):
        temp.append(a[i]-a[i-1])
    return temp
def generate_sequence(elem,succ_diff):
    list_returned=[elem]
    for i in succ_diff:
        list_returned.append(list_returned[-1]+i)
    return list_returned
for i in c:
    b=list(map(int,i.split(" ")))
    b=[-1*i for i in b[::-1]]
    temp=[]
    steps=0
    list_of_firsts=[]
    print(b)
    while [i for i in b if i!=0]!=[]:
        list_of_firsts.append(b[0])
        b=successive_difference(b)
    b.append(0)    
    while list_of_firsts!=[]:
        b=generate_sequence(list_of_firsts.pop(),b)

    sum_+=b[-1]
print(-1*sum_)
