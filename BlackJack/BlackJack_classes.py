class Player:

    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def check_money(self):
        return ("You have " + "$" + self.money + " left.")

    def sub_money(self, value):
        self.money -= value

    def add_money(self, value):
        self.money += value



    


