class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")
        return "walk"


player1 = PlayerCharacter("SaM", 20)
player2 = PlayerCharacter("Tom", 21)

print(player1.name, player1.age, player1.run())
print(player2.name, player2.age)
