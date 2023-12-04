f=open("DAY3",'r')
symbols=['@', '=', '%', '+', '$', '&', '/', '-', '#','*']
a=f.readlines()
coords=[]
set_num=[]
import re
for i in range(1,len(a)-1):
    for counter,j in enumerate(a[i]):
        if j in symbols:
            if a[i][counter-1].isdigit():
               coords.append((i,counter-1))
            #do it for all 8 directions
            if a[i][counter+1].isdigit():
                coords.append((i,counter+1))
            if a[i+1][counter].isdigit():
                coords.append((i+1,counter))
            if a[i-1][counter].isdigit():
                coords.append((i-1,counter))
            if a[i+1][counter+1].isdigit():
                coords.append((i+1,counter+1))
            if a[i-1][counter-1].isdigit():
                coords.append((i-1,counter-1))
            if a[i+1][counter-1].isdigit():
                coords.append((i+1,counter-1))
            if a[i-1][counter+1].isdigit():
                coords.append((i-1,counter+1))
for i in [0,len(a)-1]:
    for counter,j in enumerate(a[i]):
        if j in symbols:
            if a[i][counter-1].isdigit():
               coords.append((i,counter-1))
            #do it for all 8 directions
            if a[i][counter+1].isdigit():
                   coords.append((i,counter+1))
print(coords)
sum1=0
coords.sort(key=lambda x:x[1])
new_one=[]
bredd=[]
# for i,j in coords:
#     if (i,j-1) not in new_one and (i,j) not in new_one and (i,j-2) not in new_one:
#         new_one.append((i,j))
# print(len(new_one),len(coords))
for i,j in coords:
    if (i,j) in bredd:
        pass
    else:
            bredd.append((i,j))
            temp=a[i][j]
            var_1=j-1
            var_2=j+1
            while var_1>=0 and a[i][var_1].isdigit():
                temp=a[i][var_1] +temp
                bredd.append((i,var_1))
                var_1-=1
            while var_2<=145 and a[i][var_2].isdigit():
                temp+=a[i][var_2]
                bredd.append((i,var_2))
                var_2+=1
            set_num.append(int(temp))
prid=0
for i in range(0,len(a)):
    for counter,j in enumerate(a[i]):
        if j in symbols:
            cogs=[]
            dir_x=[0,1,-1]
            dir_y=[-1,0,1]
            check_diagonal_up=True
            check_diagonal_down=True
            for delx in dir_x:
                for del_y in dir_y:
                    if (delx in (-1,1) and del_y==1) and not check_diagonal_up:
                        continue
                    if (delx in (-1,1) and del_y==-1) and not check_diagonal_down:
                        continue
                    if 0<=i+delx<len(a) and 0<=counter+del_y<len(a[i]) and a[i+delx][counter+del_y].isdigit() and not (delx==0 and del_y==0):
                        if delx==0 and (del_y==-1):
                            check_diagonal_down=False
                        if delx==0 and del_y==1:
                            check_diagonal_up=False
                        temp=a[i+delx][counter+del_y]
                        var_1=counter+del_y-1
                        var_2=counter+del_y+1
                        while len(a)>var_1>=0 and a[i+delx][var_1].isdigit():
                            temp=a[i+delx][var_1] +temp
                            var_1-=1
                        while 0<=var_2<=145 and a[i+delx][var_2].isdigit():
                            temp+=a[i+delx][var_2]
                            var_2+=1
                        cogs.append(int(temp))
            if len(cogs)==2:
                prid+=cogs[0]*cogs[1]
print(prid)
