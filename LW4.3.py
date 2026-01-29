#Program 1
'''
s = {1,2,3,4,5}
s.add(6)
print(f"Added 6 in the {s} set")
s.remove(3)
print(f"Removed 3 in the {s} set")
if 2 in s:
    print("Yes, 2 is present the current set.")
else:
    print("No, 2 isnt present in the current set")
'''

#Program 2
'''
set_a = {1,2,3,4}
set_b = {3,4,5,6}
union_set = set_a.union(set_b)
print(f"Union of {set_a} and {set_b} is {union_set}")
intersect_set = set_a.intersection(set_b)
print(f"Intersection of {set_a} and {set_b} is {intersect_set}")
diff_set = set_a.difference(set_b)
print(f"Difference of {set_a} and {set_b} is {diff_set}")
'''

#Program 3
'''
student = {"name":"Alice", "age":20, "grade":"A"}
print(f"Keys and values are \n{student.items()}")
student["city"] = "Delhi"
print(f"Added new item city in \n{student.items()}")
student["age"] = 21
print(f"Updated age in \n{student.items()}")
del student['grade']
print(f"Deleted the grade with the help of del: {student}")
#We can also use student.pop("grade")
'''

#Program 4
'''
keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']
dictionary = dict(zip(keys,values))
print(f"The corresponding dictionary for the lists {keys} and {values} is {dictionary}")
'''

#Program 5
'''
str1 = "123"
print(f" when string:{str1} converted to {int(str1)}", type(int((str1))))
l = [1,2,3]
print(f" when {l} converted to {tuple(l)}", type(tuple(l)))
t = (4,5,6)
print(f" when {t} converted to {list(t)}", type(list(t)))
l1 = [(1,'A'), (2,'B')]
print(f" when {l1} converted to {dict(l1)}", type(dict(l1)))
'''

#Program 6

l = [1,2,3,4,5]
del l[2]
print(f"When 3 is deleted from the list {l}")
#Remember that in list while using del specify the index number inside the brackets whereas in dictionary specify the key to be deleted
