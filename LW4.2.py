#Program 1
'''
l = ['Apple', 'Banana', 'Chikoo', 'Pear', 'Kiwi']
print(l[1], l[4])
l[0] = 'Mango'
print(l)
l.sort()
print(f"When sorted in ascending order {l}")
l.reverse()
print(f"When reversed {l}")
'''

#Program 2
'''
t = (25, 30, 98, 65, 58)
print(t[2])
t[1] = 20
print(t)
'''
'''When tried to change an element in a tuple python shows the error as tuple object doesnt support item assignment hence we can say that tuple is immutable'''

#Program 3
'''
l = [2,4,6,8]
t = (2,4,6,8)

l[2] = 10
print(l)
t[2] = 10
print(t)
'''
'''When item of list is replaced with the other item it gets replaced easily but when tried with tuple it throws an error saying tuple does not support item assignment hence it proves that list is mutable whereas tuple is immutable'''

#Program 4

l = [1,2,3,4,5,6,7,8,9,10]
'''
ans = []
for i in l:
    ans.append(i**2)
print(ans)
'''
'''
When list comprehension is applied
ans = [i**2 for i in l]
print(ans)
'''
'''
l = [i for i in range(1,21)]
even_numbers = [j for j in l if j%2==0]
print(even_numbers)
'''
l = ["hello", "WORLD", "PyThOn"]
print(l)
'''
ans = []
for i in l:
    ans.append(i.lower())
print(ans)
'''
ans = [i.lower() for i in l]
print(f"When all the strings converted to lower case {ans}")
