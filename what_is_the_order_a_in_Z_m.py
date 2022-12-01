a = int(input("enter a: "))
m = int(input("enter m:"))

for i in range(1, m):
    if((a**i) % m == 1):
        print(i)