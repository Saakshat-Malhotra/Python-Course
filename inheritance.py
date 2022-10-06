class User:
    def sign_in(self):
        return "\nlogged in"


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left {self.num_arrows}")


wizard1 = Wizard("SaM", 50)
archer1 = Archer("Tom", 100)
print(wizard1.name, wizard1.sign_in())
wizard1.attack()
print(archer1.name, archer1.sign_in())
archer1.attack()
