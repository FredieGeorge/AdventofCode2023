f=open('/home/chef/Documents/AdventOfCode/Code/DAY13','r')
b=f.readlines()
iter_list=[]
temp=[]
def diff(l,m):
    diff_=0
    for i in range(len(l)):
        if l[i]!=m[i]:
            diff_+=1
    return diff_
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for i in b:
    if i=='\n':
        iter_list.append(temp)
        temp=[]
    else:
        temp.append(i.strip('\n'))
iter_list.append(temp)
sum_row=0
for i in iter_list:
    j=0
    while j+1<len(i):
        diff_=0
        above=j
        below=j+1
        while above>=0 and below<len(i):
            diff_+=diff(i[above],i[below])
            above-=1
            below+=1
        if diff_==1:
            sum_row+=(j+1)
            break
        j+=1
sum_column=0
for i in iter_list:
    i=transpose(i)
    j=0
    while j+1<len(i):
        diff_=0
        above=j
        below=j+1
        while above>=0 and below<len(i):
            diff_+=diff(i[above],i[below])
            above-=1
            below+=1
        if diff_==1:
            sum_column+=(j+1)
            break
        j+=1
print(100*sum_row,sum_column)