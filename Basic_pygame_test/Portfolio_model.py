class Portfolio:
    def __init__(self, gold=0, iron=0, coal=0, money=0):
        # Initialize the player's assets
        self._gold = gold
        self._iron = iron
        self._coal = coal
        self._money = money

    # Getters
    def get_gold(self):
        return self._gold

    def get_iron(self):
        return self._iron

    def get_coal(self):
        return self._coal

    def get_money(self):
        return self._money

    # Setters
    def set_gold(self, amount):
        if amount >= 0:
            self._gold = amount
        else:
            raise ValueError("Gold amount cannot be negative")

    def set_iron(self, amount):
        if amount >= 0:
            self._iron = amount
        else:
            raise ValueError("Iron amount cannot be negative")

    def set_coal(self, amount):
        if amount >= 0:
            self._coal = amount
        else:
            raise ValueError("Coal amount cannot be negative")

    def set_money(self, amount):
        if amount >= 0:
            self._money = amount
        else:
            raise ValueError("Money cannot be negative")

    # Optional: You can also define methods to add or remove resources
    def add_gold(self, amount):
        if amount > 0:
            self._gold += amount
        else:
            raise ValueError("Amount to add must be positive")

    def add_iron(self, amount):
        if amount > 0:
            self._iron += amount
        else:
            raise ValueError("Amount to add must be positive")

    def add_coal(self, amount):
        if amount > 0:
            self._coal += amount
        else:
            raise ValueError("Amount to add must be positive")

    def add_money(self, amount):
        if amount > 0:
            self._money += amount
        else:
            raise ValueError("Amount to add must be positive")

    def remove_gold(self, amount):
        if 0 <= amount <= self._gold:
            self._gold -= amount
        else:
            raise ValueError("Invalid amount of gold to remove")

    def remove_iron(self, amount):
        if 0 <= amount <= self._iron:
            self._iron -= amount
        else:
            raise ValueError("Invalid amount of iron to remove")

    def remove_coal(self, amount):
        if 0 <= amount <= self._coal:
            self._coal -= amount
        else:
            raise ValueError("Invalid amount of coal to remove")

    def remove_money(self, amount):
        if 0 <= amount <= self._money:
            self._money -= amount
        else:
            raise ValueError("Invalid amount of money to remove")