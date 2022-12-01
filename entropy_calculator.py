import math

input_string = input('Enter numerators: ')
print("\n")
n = input_string.split()
# print list
print('numerators: ', n)

input_string = input('Enter denominators: ')
print("\n")
d = input_string.split()
# print list
print('denominators: ', d)

r = int(input("enter r: "))
total = 0;

if(len(n) == len(d)):
    for i in range(len(n)):
        total += -((int(n[i])/int(d[i]))*math.log(int(n[i])/int(d[i]), r))
        print(n[i] + "/" + d[i])

print(total)