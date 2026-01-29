#Program 1
'''
for i in range(1,21):
    if i%4==0:
        continue
    print(i, end = " ")
'''

#Program 2
'''
i=1
while i<10:
    if i==7:
        i += 1
        break
    print(i, end = " ")
    i+=1
'''

#Program 3
'''
for i in "assassination":
    if i=="a" or i=="i" or i=="o":
        continue
    print(i, end = " ")
'''

#Program 4
'''
N=int(input("Enter the last number for which multiplication table is required: "))
for i in range(1,N+1):
    for j in range(1,11):
        print(i, "X", j, "=", i*j)
    print()
'''

#Program 5
'''
for r in range(1,6):
    for c in range(1,r+1):
        print(c, end = " ")
    print()
'''

#Program 6
'''
for r in range(5,0,-1):
    for c in range(5,r-1,-1):
        print(c, end = " ")
    print()
'''

#Program 7
'''
for r in range(5,0,-1):
    for c in range(r,6):
        print(c, end = " ")
    print()
'''

#Program 8
for r in range(1,6):
    for c in range(r,6):
        print(c, end = " ")
    print()
