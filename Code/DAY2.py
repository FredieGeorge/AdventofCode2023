max_red=12
max_green=13
max_blue=14
sum_=0
f=open("DAY2","r")
b=f.readlines()
counter=0
for index,a in enumerate(b):
        red=0
        green=0
        blue=0
        a=a.split(":")
        a=a[1]
        a=(a).split(";")
        for i in a:
            i=i.split(",")
            for j in i:
                  if 'red' in j:
                        if red<(int(j[0:3])):
                            red=int(j[0:3])
                  elif 'green' in j:
                        if green<(int(j[0:3])):
                            green=int(j[0:3])
                  elif 'blue' in j:
                        if blue<(int(j[0:3])):
                            blue=int(j[0:3])
                        
        sum_+=red*green*blue
print(counter)
print(sum_)