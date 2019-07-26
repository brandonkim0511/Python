
import somefunctions.complaining as cp
import datetime


# print(cp.Icantpress(cp.thatkey))

UserInput = ""
prevPressTime = 0
currentPressTime = 0



while UserInput != "Stop":
    UserInput = input("Press Enter Fast!")
    currentPressTime = int(str(datetime.datetime.now()).split(".")[1])
    # print(str(currentPressTime).split(".")[1])
    print(abs(prevPressTime - currentPressTime))
    prevPressTime = currentPressTime
    # print(datetime.datetime.now())
