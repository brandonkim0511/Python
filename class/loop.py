# while 1 == 2 : print("Chaeyoung isnot the most beautiful in Twice ")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#     print(x)
# for y in fruits:
#     print(y)
# number1 = [1, 2, 3, 4]
# number2 = [1, 2, 3, 4]
# number3 = [1, 2, 3, 4]
# number4 = [1, 2, 3, 4]
#
# cnt = 0
#
#
# for a in number1:
#     for b in number2:
#         for c in number3:
#             for d in number4:
#                 cnt += 1
#                 print(a, b, c, d, cnt)
#
#
# print(cnt)
#
#
# while True :
#     input("sdgfdf\n")
#
# oddNumberList = [1]
#
# limit = int(input(" set boundary : "))
#
# while True:
#     nextval = (oddNumberList[len(oddNumberList)- 1] + 2)
#     if nextval > limit:
#         break
#     oddNumberList.append(nextval)
#
# print(oddNumberList)


fibonacciList = [1, 1]
#
limit = int(input(" set boundary : "))

while True:
    newVal = fibonacciList[len(fibonacciList) - 1] + fibonacciList[len(fibonacciList) - 2]
    if newVal > limit:
        break
    fibonacciList.append(newVal)
print(fibonacciList)

# prepUpgraded = range(limit) # [0, 1, 2, 3, 4 , ...]
# finalArr = []
#
#
# for x in prepUpgraded :
#     temp = 0
#     for idx in range(prepUpgraded.index(x)): #[0,1]
#         temp += prepUpgraded[idx]
#     finalArr.append(temp)
#
# print(finalArr)


# fibonacciListUpgraded = []
# result = 0
#
# for x in fibonacciList:
#     print(x)
#     print('||||||||')
#     for idx in range(fibonacciList.index(x)):
#         print(range(fibonacciList.index(x)))
#         print(idx)
#         print(fibonacciList[idx])
#         print("--------")
#     # result = result + x
#         result += fibonacciList[idx]
#     fibonacciListUpgraded.append(result)
#
# print(fibonacciListUpgraded)

#
#
#


# x = 1
# while x < 1000:
#     print(x)
#     x += x
