f=open("/home/chef/Documents/AdventOfCode/Code/Day19/Day19",'r')
a=f.readlines()

a=a[:558]
def eval(string):
  string=string.split(',')
  def actual_function(list_,error):  
    nonlocal string
    diccey={'x':0,'m':1,'a':2,'s':3}
    for i in string:
        if ':' not in i:
           return i
        else:
            i=i.split(':')
            if '>' in i[0]:
                j=i[0].split('>')
                if list_[diccey[j[0]]].start>int(j[1]):
                    return i[1]   
                elif list_[diccey[j[0]]].stop-1<=int(j[1]):
                    pass       
                else:
                    #error contains list of ranges that are need to be added
                    #to the initial list
                    temp=list_[diccey[j[0]]]
                    list_[diccey[j[0]]]=range(temp.start,int(j[1])+1)
                    error.append(list_.copy())
                    list_[diccey[j[0]]]=range(int(j[1])+1,temp.stop)
                    error.append(list_.copy())
                    list_[diccey[j[0]]]=temp
                    return False
            elif '<' in i[0]:
                j=i[0].split('<')
                if list_[diccey[j[0]]].stop-1<int(j[1]) :
                    return i[1]
                elif list_[diccey[j[0]]].start>=int(j[1]):
                    pass
                else:
                    #error contains list of ranges that are need to be added
                    #to the initial list
                    temp=list_[diccey[j[0]]]
                    list_[diccey[j[0]]]=range(temp.start,int(j[1]))
                    error.append(list_.copy())
                    list_[diccey[j[0]]]=range(int(j[1]),temp.stop)
                    error.append(list_.copy())
                    list_[diccey[j[0]]]=temp
                    return False
            elif '=' in i[0]:
                j=i[0].split('=')
                if list_[diccey[j[0]]].start==int(j[1]) and list_[diccey[j[0]]].stop-1==int(j[1]):
                    return i[1]
                elif int(j[1]) not in list_[diccey[j[0]]]:
                    pass
                else:
                    #error contains list of ranges that are need to be added
                    #to the initial list
                    temp=list_[diccey[j[0]]]
                    list_[diccey[j[0]]]=range(temp.start,int(j[1]))
                    error.append(list_.copy())
                    list_[diccey[j[0]]]=range(int(j[1]),int(j[i])+1)
                    error.append(list_.copy())
                    list_[diccey[j[0]]]=range(int(j[i])+1,temp.stop)
                    error.append(list_.copy())
                    list_[diccey[j[0]]]=temp
                    return False

  return actual_function  

dict_={}
for i in a:
    i=i.split('{')
    dict_[i[0]]=eval(i[1][:-2])
final=[]
initial=[[range(1,4001),range(1,4001),range(1,4001),range(1,4001)]]
final=[]
while initial:
    error=[]
    temp=initial.pop()
    a=dict_['in'](temp,error)
    while (a!='A' and a!='R') and a:
        a=dict_[a](temp,error)
    if a=='A':
        final.append(temp)
    elif a=='R':
        pass
    elif a==False:
        for i in error:
            skip=False
            for j in i:
                if j.start==j.stop:
                    skip=True
            if not skip:
                initial.append(i)
    else:
        print("error")
    print(initial)
nos=0
for i in final:
    temp=1
    for j in i:
        temp*=len(j)
    nos+=temp
print(nos)