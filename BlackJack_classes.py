class Player:

    def __init__(self, name, money=500):
        self.name = name
        self.money = money

    def __str__(self):
        return f"""Player: {self.name} | Money: {self.money}"""

    def check_money(self):
        return ("You now have " + "$" + str(self.money) + " left.")

    def sub_money(self, value):
        self.money -= value

    def add_money(self, value):
        self.money += value