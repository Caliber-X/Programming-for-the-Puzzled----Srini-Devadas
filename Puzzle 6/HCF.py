# HCF or GCD using RECURSION
# By Caliber_X

def hcf(x, y):
    
    r = y % x
    
    if r == 0:
        return x
    else:
        return hcf(r, x)
    
print(hcf(6,4))