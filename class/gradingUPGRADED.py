# 1. with input() take an integer for a grade value

gradeList = [] # math, science, english,history design
gradeList.append(int(input("What was your Mathematics score? "))) #gradeList.insert(0, gradeList[0])
gradeList.append(int(input("What was your Science score? ")))
gradeList.append(int(input("What was your English score? ")))
gradeList.append(int(input("What was your History score? ")))
gradeList.append(int(input("What was your Design score? ")))

averageScore = (gradeList[0] + gradeList[1] + gradeList[2] + gradeList[3] + gradeList[4]) / 5

SemesterReport = """
=====SemesterReport ====
averageScore : {}
averageGrade : {}
Comment : {}
========================
"""

commentList = [{
    "grade" : "A+" ,
    "comment" : "You are an amazing and brilliant student!!"
}
,
{
    "grade" : "A",
    "comment" : "You did well!"
},
{
    "grade" : "B",
    "comment" : "You worked hard."
}
]

if averageScore >= 100 :
    print(SemesterReport.format(averageScore, commentList[0]["grade"], commentList[0]["comment"]))
elif averageScore > 90 :
    print(SemesterReport.format(averageScore, commentList[1]["grade"], commentList[1]["comment"]))
elif averageScore > 80 :
    print(SemesterReport.format(averageScore, commentList[2]["grade"], commentList[2]["comment"]))


# commentDict = {
#     "comment" :
# }
# if gradeList[0] >= 100 : print("A+")
# elif gradeList[0] > 90 : print("A")
# elif gradeList[0] > 80 : print("B")
# elif gradeList[0] > 70 : print("C")
# elif gradeList[0] > 60 : print("D")
# else: print("F")
#
# if Sscore >= 100 : print("A+")
# elif Sscore > 90 : print("A")
# elif Sscore > 80 : print("B")
# elif Sscore > 70 : print("C")
# elif Sscore > 60 : print("D")
# else: print("F")
#
# if Escore >= 100 : print("A+")
# elif Escore > 90 : print("A")
# elif Escore > 80 : print("B")
# elif Escore > 70 : print("C")
# elif Escore > 60 : print("D")
# else: print("F")
#
# if Hscore >= 100 : print("A+")
# elif Hscore > 90 : print("A")
# elif Hscore > 80 : print("B")
# elif Hscore > 70 : print("C")
# elif Hscore > 60 : print("D")
# else: print("F")
#
# if Dscore >= 100 : print("A+")
# elif Dscore > 90 : print("A")
# elif Dscore > 80 : print("B")
# elif Dscore > 70 : print("C")
# elif Dscore > 60 : print("D")
# else: print("F")

# report = """
# ========Report========
#
# Math Grade : {}
# Science Grade : {}
# English Grade : {}
# History Grade : {}
# Design Grade : {}
# Average score : {}
#
# ======================
# """
# print(report.format(gradeList[0], Sscore, Escore, Hscore, Dscore, averageScore))

# # 2. make a reporting system.
# # 3. print a reportCard like what we did at profile.py.
# 4. you have to take grade from at least 5 courses.
# 5. evaluate average
# 6. Teacher's comment : according to the average.
# 7. make Comment Dictioanry
