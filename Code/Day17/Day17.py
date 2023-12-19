import sys
def take_care(list_,index_1,index_2,index_3):
    if 0<=index_1<len(list_) and 0<=index_2<len(list_[index_1]) and 0<=index_3<len(list_[index_1][index_2]):
        return list_[index_1][index_2][index_3]
    else:
        return float('inf')
f = open("/home/chef/Documents/AdventOfCode/Code/Day17/Day17_Example", 'r')
a = [[int(i) for i in j if i != '\n'] for j in f.readlines()]
b=[[[ [] for _ in range(len(row))] for row in a] for l in range(4)]
#0 is down 1 is up 2 is left 3 is right
directions={0:[-1,0],1:[1,0],2:[0,1],3:[0,-1]}
for i in range(4):
    b[i][0][0]=[0,0]
for counter in range(150):
        for i in range(len(a)):
            for j in range(len(a[i])):
                for k in range(4):
                    minima=min(take_care(b[0],i+directions[k][0],j+directions[k][1],0),take_care(b[1],i+directions[k][0],j+directions[k][1],0),take_care(b[2],i+directions[k][0],j+directions[k][1],0),take_care(b[3],i+directions[k][0],j+directions[k][1],0))+a[i][j]
                    if minima==float('inf'):
                        pass
                    else:
                        for kk in range(4):
                            if minima==(take_care(b[kk],i+directions[k][0],j+directions[k][1],0)+a[i][j]):
                                if k==kk:
                                    if take_care(b[kk],i+directions[k][0],j+directions[k][1],1)<3 and minima<take_care(b[k],i,j,0):
                                        b[k][i][j]=[minima,take_care(b[kk],i+directions[k][0],j+directions[k][1],1)+1]
                                    else:
                                        mini=float('inf')
                                        for kkk in range(4):
                                            if kkk!=kk:
                                                mini=min(mini,take_care(b[kkk],i+directions[k][0],j+directions[k][1],0)+a[i][j])
                                        if mini!=float('inf') and mini<take_care(b[k],i,j,0):
                                            b[k][i][j]=[mini,1]
                                        break
                                else:
                                    if minima<take_care(b[k],i,j,0):
                                        b[k][i][j]=[minima,1]
                                    break

for i in b:
    for j in i:
        print(j)
    print("----------------------------")
            
