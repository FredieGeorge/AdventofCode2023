f=open("/home/chef/Documents/AdventOfCode/Code/DAY10","r")
b=f.readlines()
origin_y,origin_x=31,111
initial_y,intital_x=-1,0
dfs=[(origin_x,origin_y),(origin_x + intital_x,origin_y+initial_y)]
#up right down
direction_vecs={'L':((0,-1),(1,0)),'F':((1,0),(0,1)),'7':((0,1),(-1,0)),'J':((0,-1),(-1,0)),'|':((0,1),(0,-1)),'-':((1,0),(-1,0))}
"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile."""
while True:
    a_x,a_y=dfs[-1]
    i,j = direction_vecs[b[a_y][a_x]]
    if (a_x+i[0],a_y+i[1]) not in dfs:
        if  (a_x+j[0],a_y+j[1]) not in dfs:
                print("failure")
                break
        else:
             dfs.append((a_x+i[0],a_y+i[1]))
    else:
         if  (a_x+j[0],a_y+j[1]) not in dfs:
                dfs.append((a_x+j[0],a_y+j[1]))
         else:
               print("success")
               break
x_values=[i[0] for i in dfs]
y_values=[i[1] for i in dfs]
area=x_values[-1]*y_values[0]-x_values[0]*y_values[-1]
for i in range(len(x_values)-1):
      area+=x_values[i]*y_values[i+1]-x_values[i+1]*y_values[i]
lmao=[['◼'if i in ['L','J','7','F','|','-'] else ' 'for i in b[j] ] for j in range(len(b))]
with open("/home/chef/Documents/AdventOfCode/Code/output.txt","w") as f:
    for i in range(len(lmao)):
        f.write(''.join(lmao[i])+'\n')