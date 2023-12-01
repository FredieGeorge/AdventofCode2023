import re
f=open("DAY1","r")
a=['one','two','three','four','five','six','seven','eight','nine','1','2','3','4','5','6','7','8','9']
dict_a={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
        'nine':9,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
lines=f.readlines()
f.close()
sum=0

for i in lines:
    first=[len(i)+1,0]
    last=[len(i)+1,0]
    for j in a:
        m=re.search(j,i)
        if m:
            if first[0]>m.start():
                first[0]=m.start()
                first[1]=j
    for j in a:
        m=re.search(j[::-1],i[::-1])
        if m:
            if last[0]>m.start():
                last[0]=m.start()
                last[1]=j
    print(first,last,digits)
    sum+=(10*dict_a[first[1]]+dict_a[last[1]])
            
    
print(sum)