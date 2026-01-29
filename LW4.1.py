#Program 1
'''
f_name = input("Enter you First Name: ")
l_name = input("Enter you Last Name: ")
print(f"Hello, {l_name}, {f_name}!")
'''

#Program 2
'''
item = "apple"
price = "5.50"
print(f"The price of {item} is {price} dollars.")
'''

#Program 3
'''
str1 = input("Enter the word: ")
print("When word is reverse: ", str1[::-1])
a = str1[::-1]
b = str1.lower()
c = a.lower()
if b == c:
    print("Entered word is a Palindrome")
else:
    print("Entered word is not a Palindrome")
'''

#Program 4
'''
str1 = input("Enter the word")
print(str1.upper())
print(str1.lower())
print(str1.title())
'''

#Program 5
'''
str1 = "Machine Learning and AI are trending"
print(str1)
word = "AI"
pos = str1.find(word)
print(f"The position of AI is {pos}")
str2 = str1.replace("AI", "Artificial Intelligence")
print("\n", str1, sep = "")
print(str2)
print("data data mining and big data")
str3 = "data data mining and big data.".count("data")
print(f"In the above line data is printed {str3} times")
'''

#Program 6

'''
fruits = "apple, banana, grapes".split()
print(fruits)
m_str = ''''''My name is Chirag
I am going to be a Data Analyst
I live in Surat'''
'''print(*m_str.splitlines(), sep = "\n")
'''

#Program 7

str4 = input("Enter the sentence: ")
if str4.lower().startswith("hello") and str4.lower().endswith("world"):
    print("Sentence starts with hello and ends with world")
else:
    print("Sentence doesn't starts with hello and ends with world")
str5 = "Data123#Science!"
print(str5)
op = ""
for i in str5:
    if i.isalpha():
        op+=i
print(op)
print("Python"[::-1])
