f=open("Code/DAY8.txt","r")
c=f.readlines()
a=c[2:]
b=c[0]
print(b)
nodes={}
for i in a:
    print(i)
    nodes[i[0:3]]=(i[7:10],i[12:15])
print(nodes)
import time
curr_node="AAA"
steps=0
b=b[0:-1]
print(b)
# MGA,AAA,DPA,RDA,TLA,DGA
list_a=['AAA','MGA','DPA','RDA','TLA','DGA']
list_b=[]
all_ends_with_Z=False  
while not all_ends_with_Z:
    all_ends_with_Z=True  
    for i in list_a:
          if i[2]!="Z":
              all_ends_with_Z=False
    for i in range(len(list_a)):
            curr_node=list_a[i]
            print(curr_node,steps)
            aleph=steps%len(b)
            if b[aleph]=="R":
                    curr_node=nodes[curr_node][1]
                    steps+=1
            elif b[aleph]=="L":
                    curr_node=nodes[curr_node][0]
                    steps+=1
            a[i]=curr_node
        
    
#all of the individual nodes and instruction form closed loops so an easier way to do it is to take LCM of all the individiual paths 
#added that as a png
print(steps)