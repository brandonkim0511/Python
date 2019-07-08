# python input test.

# name = input()
# print("my name is " + name)
#
# sampleNumber = input()
# # print (type(sampleNumber))
# # print(3 + sampleNumber) : this is invalid becuase the result of input() is string by default.
# print(3 + int(sampleNumber))
name = input("What is your name? ")
age = int(input("How old are you? "))
grade = int(input("What grade are you in? "))
gender = input("What gender are you? ")
nationality = input("Where are you from? ")
birthyear = int(input("When is your birth year? "))


# gender
#
# nationality
#
# birthday

# print ("I am " + name + " and I am " + age + " years old.") : this works well, but it's not very formal.


resultForm = """
 ========Result========
name : {}
gender : {}
age 2019 : {}
age 2020 : {}
graduate at : {}
nationality : {}
40 years old in the year of : {}
=========================
"""
# print(resultForm.format(name,age,int(age) + 1,2019 + (12-int(grade)))

print(resultForm.format(name, gender, age, age + 1, 2019 + (12-grade), nationality, (40 - age) + birthyear))

# HW : Develop this.
