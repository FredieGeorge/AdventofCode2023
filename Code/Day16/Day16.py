a = open("/home/chef/Documents/AdventOfCode/Code/Day16/DAY16_Example", "r")
f = [[i for i in j if i != '\n'] for j in a.readlines()]
visited = [[False for i in j] for j in f]
list_of_rays = [[0, 0, [1, 0]]]  # [x,y,[dx,dy]]
seen = []

while list_of_rays != []:
    a = list_of_rays.pop()

    if a in seen:
        continue

    seen.append([l for l in a])
    visited[a[1]][a[0]] = True
    if f[a[0]][a[1]] =='\\':
        a[2] = [a[2][1], a[2][0]]
        a[0],a[1]=a[0]+a[2][0],a[1]+a[2][1]
        list_of_rays.append([i for i in a])
        continue
    elif f[a[0]][a[1]] =='/':
        a[2] = [-a[2][1], -a[2][0]]
        a[0],a[1]=a[0]+a[2][0],a[1]+a[2][1]
        list_of_rays.append([i for i in a])
        continue
    if a[2] == [1, 0]:
        while 0 <= a[0] <= len(f[0])-1:
            a[0] += 1
            if not 0 <= a[0] <= len(f[0])-1:
                break
            visited[a[1]][a[0]] = True

            if f[a[1]][a[0]] == '|':
                list_of_rays.append([a[0], a[1], [0, 1]])
                list_of_rays.append([a[0], a[1], [0, -1]])
                break
            elif f[a[1]][a[0]] == "\\":
                a[2] = [0, 1]
                list_of_rays.append([i for i in a])
                break
            elif f[a[1]][a[0]] == "/":
                a[2] = [0, -1]
                list_of_rays.append([i for i in a])
                break
            elif not (0 <= a[1] < len(f) and 0 <= a[0] < len(f[0])):
                break

    elif a[2] == [-1, 0]:
        while 0 <= a[0] <= len(f[0])-1:
            a[0] -= 1
            if not 0 <= a[0] <= len(f[0])-1:
                break
            visited[a[1]][a[0]] = True

            if f[a[1]][a[0]] == '|':
                list_of_rays.append([a[0], a[1], [0, 1]])
                list_of_rays.append([a[0], a[1], [0, -1]])
                break
            elif f[a[1]][a[0]] == "\\":
                a[2] = [0, -1]
                list_of_rays.append([i for i in a])
                break
            elif f[a[1]][a[0]] == "/":
                a[2] = [0, 1]
                list_of_rays.append([i for i in a])
                break
            elif not (0 <= a[1] < len(f) and 0 <= a[0] < len(f[0])):
                break

    elif a[2] == [0, 1]:
        while 0 <= a[1] <= len(f)-1:
            a[1] += 1
            if not 0 <= a[1] <= len(f)-1:
                break           
            visited[a[1]][a[0]] = True

            if f[a[1]][a[0]] == '-':
                list_of_rays.append([a[0], a[1], [1, 0]])
                list_of_rays.append([a[0], a[1], [-1, 0]])
                break
            elif f[a[1]][a[0]] == "\\":
                a[2] = [1, 0]
                list_of_rays.append([i for i in a])
                break
            elif f[a[1]][a[0]] == "/":
                a[2] = [-1, 0]
                list_of_rays.append([i for i in a])
                break
            elif not (0 <= a[1] < len(f) and 0 <= a[0] < len(f[0])):
                break

    elif a[2] == [0, -1]:
        while 0 <= a[1] <= len(f)-1:
            a[1] -= 1
            if not 0 <= a[1] <= len(f)-1:
                break  
            visited[a[1]][a[0]] = True

            if f[a[1]][a[0]] == '-':
                list_of_rays.append([a[0], a[1], [1, 0]])
                list_of_rays.append([a[0], a[1], [-1, 0]])
                break
            elif f[a[1]][a[0]] == "\\":
                a[2] = [-1, 0]
                list_of_rays.append([i for i in a])
                break
            elif f[a[1]][a[0]] == "/":
                a[2] = [1, 0]
                list_of_rays.append([i for i in a])
                break
            elif not (0 <= a[1] < len(f) and 0 <= a[0] < len(f[0])):
                break

count = 0
for i in visited:
    for j in i:
        if j:
            count += 1

print(count)
