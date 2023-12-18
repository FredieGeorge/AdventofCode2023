f=open("/home/chef/Documents/AdventOfCode/Code/DAY14",'r')
a=f.readlines()
def calculate_load(a):
  total_sum=0
  for i in transpose(a):
    for j in range(len(i)):
     if i[j]=='O':
        total_sum+=len(i)-j
  transpose(a)
  return total_sum

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
a=[[j for j in i if j!='\n'] for i in a]
def north(a):
    a=transpose(a)
    for i in a:
      for j in range(len(i)):
        if i[j]=='O' and j!=0:
            k=j-1
            while k>=0:
                if i[k]=='.':
                    temp = i[k + 1]
                    i[k + 1] = i[k]
                    i[k] = temp                
                else:
                    break
                k-=1  
    a=transpose(a)
    return a
def south(a):
    a=transpose(a)
    for i in a:
     for j in range(len(i)-1,-1,-1):
        if i[j]=='O' and j!=len(i)-1:
            k=j+1
            while k<=len(i)-1:
                if i[k]=='.':
                    temp = i[k - 1]
                    i[k - 1] = i[k]
                    i[k] = temp                
                else:
                    break
                k+=1  
    a=transpose(a)
    return a
def east(a):
    for i in a:
        for j in range(len(i)-1,-1,-1):
            if i[j]=='O' and j!=len(i)-1:
             k=j+1
             while k<=len(i)-1:
                if i[k]=='.':
                    temp = i[k - 1]
                    i[k - 1] = i[k]
                    i[k] = temp                
                else:
                    break
                k+=1
    return a  
def west(a):
    for i in a:
        for j in range(len(i)):
            if i[j]=='O' and j!=0:
             k=j-1
             while k>=0:
                if i[k]=='.':
                    temp = i[k + 1]
                    i[k + 1] = i[k]
                    i[k] = temp                
                else:
                    break
                k-=1
    return a
for i in a:
    print(i)
print("---------------")
i=1
seen=[]
while i<=1000000000:
    a=north(a)
    a=west(a)
    a=south(a)
    a=east(a)
    if a not in seen:
            seen.append(a)
            i+=1

    else:
        break


first_index=seen.index(a)
print(calculate_load(seen[first_index-1 + (1000000000-first_index)%(len(seen)-first_index)]))

