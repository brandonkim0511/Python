# class Person:
#   def __init__(s, name, age):
#     s.name = name
#     s.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)

class girlGroup :
    def __init__(self, member, song, name):
        self.name = name
        self.member = member
        self.song = song

    def introduce(self, quote) :
        for eachMember in self.member :
            print(quote + " I am " + eachMember +  " of  " +self.name )


class Twice(girlGroup) :
    def __init__(self, member, song, nationality, race, name):
        girlGroup.__init__(self, member, song, name)
        self.nationality = nationality
        self.race = race
        # self.seongByeol = gender
        # self.Nai = age


# Chaeng = Twice("girl", 20)
# print(Chaeng.seongByeol)
# print(Chaeng.Nai)

koreanTwice = Twice(["NY", "MM", "SN"], "DtNA", "Korea", "asian", "Twice")
koreanTwice.introduce("One in a million~! ")
blackPink = girlGroup(["JS", "JN", "RS"], "KtL", "blackPink")
blackPink.introduce("One in a Trillion ~ ! ")
