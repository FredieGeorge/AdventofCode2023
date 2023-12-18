f=open("/home/chef/Documents/AdventOfCode/Code/DAY14",'r')
a=f.readlines()
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
a=transpose(a)
def find_in_list(list_,value):
    for i in range(len(list_)):
        if list_[i]==value:
            return i
    return -1
total_sum=0
b=[[j for j in i] for i in a]
for i in a[:-1]:
    lastpos=find_in_list(i,'.')
    for j in range(len(i)):
        if i[j]=='#':
            k=j+1
            while k<=len(i)-2:
                    if i[k]=='.':
                        lastpos=k
                        break
                    k+=1
        elif i[j]=='O':
            if j>lastpos:
                i[j]='.'
                i[lastpos]='O'
                k=lastpos+1
                while k<=len(i)-2:
                    if i[k]=='.':
                        lastpos=k
                        break
                    k+=1
    for j in range(len(i)):
        if i[j]=='O':
            total_sum+=len(i)-j

for i in range(len(b)):
    print(a[i] ,"\n", b[i])
print(a==b)