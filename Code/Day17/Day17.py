import sys
def take_care(list_,index_1,index_2,index_3):
    if 0<=index_1<len(list_) and 0<=index_2<len(list_[index_1]) and 0<=index_3<len(list_[index_1][index_2]):
        return list_[index_1][index_2][index_3]
    else:
        return float('inf')
def take_care_2(list_,index_1,index_2):
    if 0<=index_1<len(list_) and 0<=index_2<len(list_[index_1]):
        return list_[index_1][index_2]
    else:
        return float('inf')
f = open("/home/chef/Documents/AdventOfCode/Code/Day17/Day17_Example", 'r')
a = [[int(i) for i in j if i != '\n'] for j in f.readlines()]
b=[[[ [] for _ in range(len(row))] for row in a] for l in range(4)]
#0 is down 1 is up 2 is left 3 is right
directions={0:[-1,0],1:[1,0],2:[0,1],3:[0,-1]}
for i in range(4):
    b[i][0][0]=[0,0]
temp=[]
exit=False
count=0
while count<=100:
        exit=True
        for i in range(len(a)):
            for j in range(len(a[i])):
                for k in range(4):
                    min_=(float('inf'),0)
                    for kk in range(4):
                        if k==kk:
                            continue
                        for num in range(4,11):
                            sum_=0
                            for jem in range(0,num):
                                sum_+=take_care_2(a,i+jem*directions[k][0],j+jem*directions[k][1])
                            sum_+=take_care(b[kk],i+num*directions[k][0],j+num*directions[k][1],0)
                            if min_[0]>sum_:
                                min_=(sum_,num)
                    if min_[0]!=float("inf") and take_care(b[k],i,j,0)>min_[0]:
                        b[k][i][j]=[min_[0],min_[1]]
                        exit=False
        count+=1
print(count)
for i in b:
    print(i[-1])

         
