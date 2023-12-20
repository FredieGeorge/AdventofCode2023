from math import lcm
def return_first_common(a_1,d_1,a_2,d_2):
    #return first common element of aps a_1,a_1+d_1,a_1+2*d_1,... and a_2,a_2+d_2,a_2+2*d_2,...
    #return False if no common element

    #find first common element of a_1 and a_2
    i=0
    j=0
    while a_1+i*d_1!=a_2+j*d_2:
        if a_1+i*d_1<a_2+j*d_2:
            i+=1
        else:
            j+=1
    return a_1+i*d_1
a=return_first_common(3919,3919,4027,4027)
b=return_first_common(4007,4007,3917,3917)
c=return_first_common(a,lcm(3919,4027),b,lcm(4007,3917))
print(c)