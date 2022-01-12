"""STRINGS"""

character_name = "Jim"
character_age = "50"
print("There once was a man named " + character_name + ", ")
print("he was " +character_age+ " years old. ")

character_name = "Sean"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

print("Python\nPractice")
print("Python\"Practice")
print("Python\Practice")

phrase = "Python Practice"
print(phrase)

phrase = "Python Practice"
print(phrase + " is fun")

phrase = "Python Practice"
print(phrase.lower())

phrase = "Python Practice"
print(phrase.upper())

phrase = "Python Practice"
print(phrase.isupper())

phrase = "Python Practice"
print(phrase.upper().isupper())

phrase = "Python Practice"
print(len(phrase))

phrase = "Python Practice"
print(phrase[0])

phrase = "Python Practice"
print(phrase.index("P"))

phrase = "Python Practice"
print(phrase.index("a"))

phrase = "Python Practice"
print(phrase.index("Prac"))

phrase = "Python Practice"
print(phrase.replace("Python", "Javascript"))


"""NUMBERS"""

print(2)
print(2.0872)
print(3 + 2)
print(3 * 4)
print(3 * 4 + 5)
print(3 *(4 + 5))
print(10 % 3)

my_num = 5
print(my_num)
print(str(my_num) + " my favorite number")

my_num = -5
print(abs(my_num))
print(pow(3, 2))
print(max(4,6))
print(min(4,6))
print(round(3.2))
print(round(3.6))

"""importing a moduel"""
from math import *
my_num = -5
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))



"""USER_INPUT"""

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)