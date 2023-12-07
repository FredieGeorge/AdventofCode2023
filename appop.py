def range_in_range(a, b):
    return (a.start in b and a.stop in b) or (a.start not in b and a.stop not in b)
def binary_search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if mid == len(nums) - 1 and nums[mid] <= target:
            return mid
        elif nums[mid] <= target < nums[mid + 1]:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if target < nums[0]:
        return -1
    else:
        return len(nums) - 1

def function_generator(string, inps):
    func_def = []
    string = string.split('\n')
    
    for i in string:
        b = list(map(int, i.split(' ')))
        del_ = b[0] - b[1]
        func_def.append((range(b[1], b[1] + b[2]), del_))
    
    func_def.sort(key=lambda x: x[0].start)
    a = [i[0].start for i in func_def]
    a.append(func_def[-1][0].stop)
    
    temp = []
    for i in inps:
        beginning = binary_search(a, i.start)
        end = binary_search(a, i.stop)
        
        if beginning == end:
            temp.append(i)
        else:
            temp.append(range(i.start, a[beginning + 1]))
            temp.append(range(a[end], i.stop))
            l = beginning + 1
            while l + 1 <= end:
                temp.append(range(a[l], a[l + 1]))
                l += 1
    inps = []
    print(temp)
    for i in temp:
        add_nothing=True
        for j in func_def:
            if i.start in j[0]:
                inps.append(range(i.start + j[1], i.stop + j[1]))
                add_nothing=False
                break
        if add_nothing:
            inps.append(i)

    return inps


    

seed_to_soil="""50 98 2
52 50 48"""

soil_to_fertilizer="""0 15 37
37 52 2
39 0 15"""

fertilizer_to_water ="""49 53 8
0 11 42
42 0 7
57 7 4"""

water_to_light ="""88 18 7
18 25 70"""

light_to_temperature ="""45 77 23
81 45 19
68 64 13"""

temperature_to_humidity="""0 69 1
1 0 69"""

humidity_to_location ="""60 56 37
56 93 4"""


new_seeds=[]
seeds=[79,14,55,13]
for i in range(len(seeds)//2):
    new_seeds.append(range(seeds[2*i],seeds[2*i]+seeds[2*i+1]))
print(new_seeds)
a1=function_generator(seed_to_soil,new_seeds)
# a2=function_generator(soil_to_fertilizer,a1)
# a3 =function_generator(fertilizer_to_water,a2)
# a4 =function_generator(water_to_light,a3)
# a5 =function_generator(light_to_temperature,a4)
# a6 =function_generator(temperature_to_humidity,a5)
# a7 =function_generator(humidity_to_location,a6)
print(a1)