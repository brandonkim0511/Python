# 1. with input() take an integer for a grade value

Mscore = int(input("What was your Mathematics score? "))
Sscore = int(input("What was your Science score? "))
Escore = int(input("What was your English score? "))
Hscore = int(input("What was your History score? "))
Dscore = int(input("What was your Design score? "))
averageScore = (Mscore + Sscore + Escore + Hscore + Dscore) / 5

if Mscore == 100 : print("A+")
elif Mscore > 90 : print("A")
elif Mscore > 80 : print("B")
elif Mscore > 70 : print("C")
elif Mscore > 60 : print("D")
else: print("F")

if Sscore == 100 : print("A+")
elif Sscore > 90 : print("A")
elif Sscore > 80 : print("B")
elif Sscore > 70 : print("C")
elif Sscore > 60 : print("D")
else: print("F")

if Escore == 100 : print("A+")
elif Escore > 90 : print("A")
elif Escore > 80 : print("B")
elif Escore > 70 : print("C")
elif Escore > 60 : print("D")
else: print("F")

if Hscore == 100 : print("A+")
elif Hscore > 90 : print("A")
elif Hscore > 80 : print("B")
elif Hscore > 70 : print("C")
elif Hscore > 60 : print("D")
else: print("F")

if Dscore == 100 : print("A+")
elif Dscore > 90 : print("A")
elif Dscore > 80 : print("B")
elif Dscore > 70 : print("C")
elif Dscore > 60 : print("D")
else: print("F")

report = """
========Report========

Math Grade : {}
Science Grade : {}
English Grade : {}
History Grade : {}
Design Grade : {}
Average score : {}

======================
"""
print(report.format(Mscore, Sscore, Escore, Hscore, Dscore, averageScore))

# # 2. make a reporting system.
# # 3. print a reportCard like what we did at profile.py.
# 4. you have to take grade from at least 5 courses.
# 5. evaluate average
# 6. Teacher's comment : according to the average.
# 7. make Comment Dictioanry
