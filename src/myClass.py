class Person:
    name = ""
    wallet = None
    bike = None

    def __init__(self, name):
        self.name = name
        m = "A person "
        m += self.name
        m += " is here."

    def setWallet(self, wallet):
        self.wallet = wallet
        m = self.name
        m += " has the new wallet."
        print(m)

    def rentBike(self, bike):
        self.wallet.balance -= 50
        self.bike = bike
        m = self.name
        m += " 's wallet now has "
        m += str(self.wallet.balance)
        m += " dollars"
        print(m)

class ElectronWallet:
    balance = 0
    person = None

    def __init__(self, person, balance):
        self.person = person
        self.balance = balance
        m = "A new wallet has "
        m += str(self.balance)
        m += " dollars"
        print(m)


class RenterBike:
    person = None

    def __init__(self, person):
        self.person = person
        m = "A bike is rented by "
        m += str(self.person.name)
        m += "."
        print(m)


someone = Person("John")
newWallet = ElectronWallet(someone, 1000)
someone.setWallet(newWallet)
newbike = RenterBike(someone)
someone.rentBike(newbike)