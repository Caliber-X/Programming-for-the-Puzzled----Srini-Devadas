# This Code was taken from TELEGRAM
# Embedded -->for u
# By Caliber_X

def pow(a, b):

    if (b == 0): 
        return 1
    
    res = 0
 
    power = pow(a, b - 1)
 
 
    # for i in range(a):
    #     res += power

    res += power * a
     
    return res

print(pow(7, 3))