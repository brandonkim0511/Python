# def plus (plus1, plus2):
#     # print(plus1 + plus2)
#     plus1 -= 3
#     return(plus1 + plus2)
#     print("sdgfhdsa")
#
# print(plus(5, 3))
#
#
#
#
# def saySomething() :
#     a = print("NY is best twice memeber")
#     print(a)
#
#
#
# # print()
# # input()
# # built-in function
#
# print(saySomething())
#
#
#
#
# # ((5+3) + 7)
#
# print(  plus( plus(5,3) , 7 )      )
#

# for x in ["NY", "MM", "SN"] :
#     print(x + "is beautiful")


# def praiseTwice (bestMember, secondBestMember) :
#     print("{} is the best twice Member".format(bestMember))
#     print("{} is the second best twice Member".format(secondBestMember))
#
# praiseTwice("Nayeon", "Sana")

def factorial (number):
    if number > 0:
        result = number * factorial(number - 1)
    else : result = 1
    return result

print ( factorial (    int(input("Type in a number : "))    ) )
