def hash_first(list_,no):
    #no[0] entries should be not .
    possible=1
    if no[0]>len(list_):
        return 0
    for i in range(no[0]):
        if list_[i]=='.':
            possible=0
            break
    if len(no)==1:
        return possible
    if possible and ((no[0]<len(list_) and list_[no[0]]!='#') or no[0]==len(list_)):
        return possibilites(list_[no[0]+1:],no[1:])
    else:
        return 0
def dot_first(list_,no):
    if len(list_)==1:
        return 0
    else:
        return possibilites(list_[1:],no)

def possibilites(list_,no):
    sum=0
    if len(no)==0:
        if '#' not in list_:
            return 1
        else:
            return 0
    if list_[0]=='#':
        sum+=hash_first(list_,no)
    elif list_[0]=='.':
        sum+=dot_first(list_,no)
    else:
        sum+=dot_first(list_,no) + hash_first(list_,no)
    return(sum)

final_sum=0
input_=[]
f=open('/home/chef/Documents/AdventOfCode/Code/DAY12','r')
b=f.readlines()
for i in b:
    i=i.split(' ')
    input_.append((i[0],list(map(int,i[1].split(',')))))
for i in input_[0:]:
    final_sum+=possibilites(i[0],i[1])
    print(i,possibilites(i[0],i[1]))
print(final_sum)