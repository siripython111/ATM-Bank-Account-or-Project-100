#Code
class BankMoney(object):
    def __init__(self, name, moneyHave, moneyGet, moneyLeft=None):
        self.name = name
        self.moneyHave = moneyHave
        self.moneyGet = moneyGet
        self.moneyLeft = moneyLeft or {}

    def setMoneyLeft(self, moneyHave, moneyGet):
        self.moneyLeft[moneyHave, moneyGet] = moneyHave

    def getMoneyHave(self, moneyHave):
        return self.moneyHave

    def getMoneyLeft(self):
        return ((self.moneyHave) - (self.moneyGet))

    def getName(self):
        print("Jill")

#some person
jill = ("Jill", 50, 15, {50: 15})
    
#get the money left after buying
print(jill.MoneyLeft())
    