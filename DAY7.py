#brute force for the win
def basefourteen(a):
    num = 0
    dict_values = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    for i in range(len(a)):
        if a[i].isdigit():
            num += int(a[i]) * 15 ** (len(a) - i - 1)
        else:
            num += dict_values[a[i]] * (15 ** (len(a) - i - 1))
    return num

f = open("DAY7", "r")
a = f.readlines()
b = []
for i in a:
    i = i.replace("\n", "")
    dum, bo = i.split()
    b.append((dum, int(bo)))

def check(a):
    if 'J' not in a:
        a = sorted(a)
        if a[0] == a[1] == a[2] == a[3] == a[4]:
            return 7
        elif a[0] == a[1] == a[2] == a[3] or a[1] == a[2] == a[3] == a[4]:
            return 6
        elif (a[0] == a[1] == a[2] and a[3] == a[4]) or (a[0] == a[1]  and a[2]==a[3] == a[4]):
            return 5
        elif a[0] == a[1] == a[2] or a[1] == a[2] == a[3] or a[2] == a[3] == a[4]:
            return 4
        elif (a[0] == a[1] and a[2] == a[3]) or (a[0] == a[1] and a[3] == a[4]) or (a[1] == a[2] and a[3] == a[4]):
            return 3
        elif a[0] == a[1] or a[1] == a[2] or a[2] == a[3] or a[3] == a[4]:
            return 2
        else:
            return 1
    else:
        shabdha=0
        for i in ['2','3','4','5','6','7','8','9','T','Q','K','A']:
            b=a.replace('J',i)
            b = sorted(b)
            if b[0] == b[1] == b[2] == b[3] == b[4]:
                al= 7
            elif b[0] == b[1] == b[2] == b[3] or b[1] == b[2] == b[3] == b[4]:
                al= 6
            elif (b[0] == b[1] == b[2] and b[3] == b[4]) or (b[0] == b[1]  and b[2]==b[3] == b[4]):
                al= 5
            elif b[0] == b[1] == b[2] or b[1] == b[2] == b[3] or b[2] == b[3] == b[4]:
                al= 4
            elif (b[0] == b[1] and b[2] == b[3]) or (b[0] == b[1] and b[3] == b[4]) or (b[1] == b[2] and b[3] == b[4]):
                al= 3
            elif b[0] == b[1] or b[1] == b[2] or b[2] == b[3] or b[3] == b[4]:
                al= 2
            else:
                al= 1
            shabdha=max(shabdha,al)
        return shabdha
dict_rank = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
for i in b:
    dict_rank[check(i[0])].append(i)

lmao = []
for i in range(1, 8):
    dict_rank[i].sort(key=lambda x: basefourteen(x[0]))
    print(dict_rank[i])
    lmao.extend(dict_rank[i])
sum_=0
for i in range(len(lmao)):
    sum_+=lmao[i][1]*(i+1)
print(sum_)