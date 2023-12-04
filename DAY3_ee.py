f = open("DAY3", 'r')
symbols = ['@', '=', '%', '+', '$', '&', '/', '-', '#', '*']
a = f.readlines()
cogs = []

def collect_digits(row, start_col, step):
    temp = a[row][start_col]
    var = start_col + step

    while 0 <= var < len(a[row]) and a[row][var].isdigit():
        temp = a[row][var] + temp if step == -1 else temp + a[row][var]
        var += step

    return int(temp)

for i in range(1, len(a) - 1):
    for counter, j in enumerate(a[i]):
        if j in symbols:
            # Check in both upward, downward, and diagonal directions for neighboring numbers
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    ni, nj = i + dx, counter + dy

                    # Check if indices are within bounds and the character is a digit
                    if 0 <= ni < len(a) and 0 <= nj < len(a[i]) and a[ni][nj].isdigit():
                        cogs.append(collect_digits(ni, nj, dy) + collect_digits(ni, nj, -dy))

print("Cog Numbers:", cogs)
print(sum(cogs))
f.close()
