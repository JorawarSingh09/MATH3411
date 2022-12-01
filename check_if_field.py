import math

#check if Z_m is a field 
def check(m):
    for i in range(1, m):
        for j in range(1, m):
            if((i * j) % m == 0): return False
    return True

m = int(input("enter size of field: "))
if(check(m)):
    print("is a field")
else:
    print("not a field")