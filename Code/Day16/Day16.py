a = open("/home/chef/Documents/AdventOfCode/Code/Day16/DAY16", "r")
f = [[i for i in j if i != '\n'] for j in a.readlines()]
ans=0
for i in range(len(f)):
    for j in range(len(f[i])):
           for k in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            list_of_rays = [[i,j,k]]  # [x,y,[dx,dy]]
            visited = [[False for i in j] for j in f]
            seen = []

            while list_of_rays != []:
                a = list_of_rays.pop()
                if a in seen:
                    continue
                seen.append([l for l in a])
                while 0 <= a[0] <= len(f[0])-1 and 0<=a[1]<=len(f)-1:
                    visited[a[1]][a[0]] = True
                    if f[a[1]][a[0]] == '|':
                        if a[2][1]==0:
                            list_of_rays.append([a[0], a[1], [0, 1]])
                            list_of_rays.append([a[0], a[1], [0, -1]])
                            break
                    elif f[a[1]][a[0]]=="-":
                        if a[2][0]==0:
                            list_of_rays.append([a[0], a[1], [1, 0]])
                            list_of_rays.append([a[0], a[1], [-1, 0]])
                            break
                    elif f[a[1]][a[0]] == '\\':
                        a[2] = [a[2][1], a[2][0]]
                        a[0],a[1]=a[0]+a[2][0],a[1]+a[2][1]
                        list_of_rays.append([i for i in a])
                        break
                    elif f[a[1]][a[0]] == '/':
                        a[2] = [-a[2][1], -a[2][0]]
                        a[0],a[1]=a[0]+a[2][0],a[1]+a[2][1]
                        list_of_rays.append([i for i in a])
                        break 
                    a[0],a[1]=a[0]+a[2][0],a[1]+a[2][1]
            count = 0
            for ii in visited:
                for jj in ii:
                    if jj:
                        count += 1

            ans=max(ans,count)
            print(ans,i)
# it is possible to speed up the function  for second part by making it recursive and using some caching but im too lazy to do that