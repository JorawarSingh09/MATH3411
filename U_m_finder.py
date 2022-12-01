import math

m = int(input('Enter m:'))
elements = []
count = 0
print(m)

for i in range(m):
    if(math.gcd(i, m) == 1):
        count += 1
        elements.append(i)
print("elements: " + str(elements))
print("Eulers function / phi = "  + str(count))