f=open("/home/chef/Documents/AdventOfCode/Code/Day20/Day20",'r')
a=f.readlines()
print(a)

"""
% intially 0 if pulse==0 negate state
& keep a list of pulses recieved, if all are 1 send 0 else send 1
'broadcaster' recieves pulse and sends it to all of the connected ones
some of them withou


"""
rx=1
dict_={}
for i in a:
    i=i.split(' -> ')
    if '%' in i[0]:
            i[0]=i[0].split('%')
            i[1]=i[1][:-1].split(',')
            i[1]=[ll.strip() for ll in i[1]]
            dict_[i[0][1]]=['%',i[1],0,[]]#type,forward_connections,state,pulse
    elif '&' in i[0]:
            i[0]=i[0].split('&')
            i[1]=i[1][:-1].split(',')
            i[1]=[ll.strip() for ll in i[1]]

            dict_[i[0][1]]=['&',i[1],dict()]#type,forward,memory,
    else:
         i[1]=i[1][:-1].split(',')
         i[1]=[ll.strip() for ll in i[1]]

         dict_[i[0]]=['=',i[1],0]#type,forward,received
#initialise the recieved dicts for &
for i in dict_.keys():
     for j in dict_[i][1]:
          if j in dict_.keys() and dict_[j][0]=='&':
               dict_[j][2][i]=0
low_count=0
high_count=0
oo={}
for ll in ['ng','qb','qt','mp']:
    oo[ll]=[]
counter=1
while counter<100_000:
            todo=['broadcaster']
            low_count+=1
            while todo:
                temp=todo.pop(0)
                if '%' == dict_[temp][0]:
                        pulse=dict_[temp][3].pop(0)
                        if pulse==1:
                            pass
                        else:
                            dict_[temp][2]=not dict_[temp][2]
                            if dict_[temp][2]==1:
                                high_count+=len(dict_[temp][1])
                            else:
                                    low_count+=len(dict_[temp][1])
                            for ii in dict_[temp][1]:
                                if ii not in dict_.keys():
                                    continue
                                todo.append(ii)
                                if dict_[ii][0]=='%':
                                    dict_[ii][3].append(dict_[temp][2])
                                elif dict_[ii][0]=='&':
                                    dict_[ii][2][temp]=dict_[temp][2]
                                elif dict_[ii][0]=='=':
                                    dict_[ii][2]=dict_[temp][2]
                            
                elif '&'== dict_[temp][0]:
                        poop=1
                        for value in dict_[temp][2].values():
                            poop= poop and value
                        poop=not poop
                        if poop==1:
                                for ll in ['ng','qb','qt','mp']:
                                      if temp==ll:
                                        oo[ll].append(counter)
                                high_count+=len(dict_[temp][1])
                        else:
                                    low_count+=len(dict_[temp][1])
                        for ii in dict_[temp][1]:
                                if ii not in dict_.keys():
                                    continue
                                todo.append(ii)

                                if dict_[ii][0]=='%':
                                    dict_[ii][3].append(poop)
                                elif dict_[ii][0]=='&':
                                    dict_[ii][2][temp]=poop
                                elif dict_[ii][0]=='=':
                                    dict_[ii][2]=poop
                else:
                    if dict_[temp][2]==1:
                                high_count+=len(dict_[temp][1])
                    else:
                                low_count+=len(dict_[temp][1])
                    for ii in dict_[temp][1]:
                                if ii not in list(dict_.keys()):
                                    continue
                                todo.append(ii)
                                if dict_[ii][0]=='%':
                                    dict_[ii][3].append(dict_[temp][2])
                                elif dict_[ii][0]=='&':
                                    dict_[ii][2][temp]=dict_[temp][2]
                                elif dict_[ii][0]=='=':
                                    dict_[ii][2]=dict_[temp][2]
            counter+=1
print(oo)