students = [{"id":101, "name":"Alice", "score":85}, {"id":102, "name":"Bob", "score":78}, {"id":103, "name":"Charlie", "score":92}]
print(f"ID: {students[0]["id"]} Name: {students[0]["name"]:<7} Score: {students[0]["score"]}")
print(f"ID: {students[1]["id"]} Name: {students[1]["name"]:<7} Score: {students[1]["score"]}")
print(f"ID: {students[2]["id"]} Name: {students[2]["name"]:<7} Score: {students[2]["score"]}")
add = 0
for stu in students:
    print(f"The name of student is {stu["name"]}")
    score = stu.get("score")
    add += score
avg = add/len(students)
print(f"The average score of all students is {avg}")
'''
new_id = int(input("Enter the id of student"))
new_name = input("Enter the name of student")
new_score = int(input("Enter the score of student"))
students.append({"id":new_id, "name":new_name, "score":new_score})
print(students)
students[1]["score"] = 88
print(students)
'''
'''
students.pop(2)
print(students)
for stu in students:
    if stu["score"] > 80:
        print(stu)
'''

from operator import itemgetter
sort_student = sorted(students, key=itemgetter("score"), reverse=True)
print(sort_student)

highest_score = students[0]
for stu in students:
    if stu["score"]>highest_score["score"]:
        highest_score = stu
print(f"The student with highest score is {highest_score["name"]}")

count_A = 0
count_B = 0
count_C = 0
for stu in students:
    if stu["score"]>=90:
        print(f"Name: {stu["name"]} | Score: {stu["score"]} | Grade: A")
        count_A += 1
    elif stu["score"]<80:
        print(f"Name: {stu["name"]} | Score: {stu["score"]} | Grade: C")
        count_C += 1
    elif stu["score"]<90:
        print(f"Name: {stu["name"]} | Score: {stu["score"]} | Grade: B")
        count_B += 1
print(f"Total students with Grade A= {count_A}")
print(f"Total students with Grade B= {count_B}")
print(f"Total students with Grade C= {count_C}")


