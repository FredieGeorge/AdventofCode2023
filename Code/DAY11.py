f=open('/home/chef/Documents/AdventOfCode/Code/DAY11','r')
a=[[i for i in j if i!='\n'] for j in f.readlines()]
def double_x(l):
    lmao=[]
    for i in range(len(l)):
        add_two=True
        for j in l[i]:
            if j!='.':
                add_two=False
        if add_two:
            lmao.append(i)
    return lmao
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
def binary_search_less_than(l,x):
    if x<l[0]:
        return -1
    if x>l[-1]:
        return len(l)-1
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return high
extra=1000000
list_x=double_x(a)
list_y=double_x(transpose(a))
list_of_vetices=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]!='.':
            list_of_vetices.append((i,j))
sum_of_edges=0
for i in range(len(list_of_vetices)):
    for j in range(i,len(list_of_vetices)):
        sum_of_edges += abs(list_of_vetices[i][0]-list_of_vetices[j][0])+abs(list_of_vetices[i][1]-list_of_vetices[j][1])
        
        sum_of_edges+=(abs(binary_search_less_than(list_x,list_of_vetices[i][0])-binary_search_less_than(list_x,list_of_vetices[j][0]))+abs(binary_search_less_than(list_y,list_of_vetices[i][1])-binary_search_less_than(list_y,list_of_vetices[j][1])))*(extra-1)
print(sum_of_edges)                                                                                                                                                
