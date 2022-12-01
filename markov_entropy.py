import math

input_string = input('Enter M_1: ')
print("\n")
m_1 = input_string.split()
# prfloat list
print('m_1: ', m_1)

input_string = input('Enter M_2: ')
print("\n")
m_2 = input_string.split()
# prfloat list
print('m_2: ', m_2)

input_string = input('Enter P Numerator: ')
print("\n")
pn = input_string.split()
# prfloat list

input_string = input('Enter P denominator: ')
print("\n")
pd = input_string.split()
# prfloat list

for i in range(len(pn)):
    print(pn[i] + "/" + pd[i])

r = float(input("enter r: "))
H_S = []
total1 = 0
total2 = 0
if(len(m_1) == len(m_2)):
    for i in range(len(m_1)):
        #calculate H(S|S_1)
        print(-1*float(m_1[i])*math.log(float(m_1[i])), r)
        total1 += (-1*float(m_1[i])*math.log(float(m_1[i]), r))
        total2 += (-1*float(m_2[i])*math.log(float(m_2[i]), r))

    H_S.append(total1)
    H_S.append(total2)
    print(H_S)

M_entropy = 0
for i in range(len(H_S)):
    M_entropy += ((int(pn[i])/int(pd[i]))*H_S[i])
print("entropy ===============")
print(M_entropy)