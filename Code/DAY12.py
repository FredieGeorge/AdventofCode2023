def possibilites(list_,no):
    sum=0
    #find first occurence of #
    if no==[]:
        return sum

    last=list_.find('#')
    first=max(0,last-no[0]+1)
    if last==-1 or len(no)!=1:
        first=0
        last=len(list_)-1
    for i in range(first,last+1):
        if i+no[0]<=len(list_):
            POSSIBLE=True
            for j in range(i,i+no[0]):
                if list_[j]=='.':
                    POSSIBLE=False
                    break
            if POSSIBLE:
                if ((i-1>=0 and list_[i-1]!='#') or i==0) and ((i+no[0]<len(list_) and list_[i+no[0]]!='#') or i+no[0]==len(list_)):
                    if len(no)==1:
                        sum+=1
                    else:  
                        sum+=possibilites(list_[i+no[0]+1:],no[1:])
    return(sum)
final_sum=0
input_=[]
f=open('/home/chef/Documents/AdventOfCode/Code/DAY12','r')
b=f.readlines()
for i in b:
    i=i.split(' ')
    input_.append((i[0],list(map(int,i[1].split(',')))))
for i in input_:
    final_sum+=possibilites(i[0],i[1])
print(final_sum)