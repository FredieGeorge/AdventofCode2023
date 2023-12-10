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

# arbit_x,arbit_y=(0,)
# lmao=[[i for i in b[j]] for j in range(len(b))]
# tofill=[(arbit_x,arbit_y)]
# counter= 0
# while tofill!=[]:
#       a_x,a_y=tofill.pop()
#       if (a_x,a_y) not in dfs and lmao[a_y][a_x]!="#":
#             lmao[a_y][a_x]="#"
#             counter+=1
#             if 0  <=a_y+1<len(b) and 0<=a_x<len(b[0]):
#                 tofill.append((a_x,a_y+1))
#             if 0  <=a_y-1<len(b) and 0<=a_x<len(b[0]):
#                 tofill.append((a_x,a_y-1))
#             if 0  <=a_y<len(b) and 0<=a_x+1<len(b[0]):
#                 tofill.append((a_x+1,a_y))
#             if 0  <=a_y<len(b) and 0<=a_x-1<len(b[0]):
#                 tofill.append((a_x-1,a_y))
#       print(counter)
# #write lmao to a txt file and save it as output.txt
# f=open("/home/chef/Documents/AdventOfCode/Code/output.txt","w")
# for i in lmao:
#     for j in i:
#         f.write(j)
#     f.write("\n")
# f.close()