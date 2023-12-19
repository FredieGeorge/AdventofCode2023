f=open("/home/chef/Documents/AdventOfCode/Code/Day18/Day18",'r')
a=f.readlines()
perimeter=[]
curr=[0,0]
def dehash(str):
    dict_=['R','D','L','U']
    return (dict_[int(str[7])],int(str[2:7],16))


for i in range(len(a)):
    a[i]=a[i].split(' ')
    a[i]=dehash(a[i][2])
    match a[i][0]:
        case 'R':
                curr[0]+=int(a[i][1])*(1)
        case 'D':
            curr[1]+=int(a[i][1])*(-1)
        case 'L':
            curr[0]+=int(a[i][1])*(-1)
        case 'U':
            curr[1]+=int(a[i][1])*(1)
        case _:
            print("Error")
    perimeter.append(curr.copy())
#pieks formula A=p/2 +i -1 from day10
#tocalc actual perimeter
actual_perimeter=0
for i in range(len(perimeter)-1):
    actual_perimeter+=abs(perimeter[i][0]-perimeter[i+1][0])+abs(perimeter[i][1]-perimeter[i+1][1])
actual_perimeter+=abs(perimeter[0][0]-perimeter[-1][0])+abs(perimeter[0][1]-perimeter[-1][1])
#shoelace formula for area of polygon
area=0
for i in range(len(perimeter)-1):
    area+=perimeter[i][0]*perimeter[i+1][1]-perimeter[i+1][0]*perimeter[i][1]
area+=perimeter[0][0]*perimeter[-1][1]-perimeter[-1][0]*perimeter[0][1]
area=abs(area)/2
pp=area+1+(actual_perimeter)/2
print(pp)