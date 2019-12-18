class MenuItem:
    def __init__(self, name=None, types=None, price=None, description=None):
        self._name = name
        self._types = types
        self._price = price
        self._description = description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def types(self):
        return self._types

    @types.setter
    def types(self, types):
        self._types = types

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def __str__(self):
        return "{} ({}): ${}, {}".format(
            self._name, self._types, self._price, self._description)

# restaurant = MenuItem(name='Fresh Spring ROlls', types='Appetizer', price=400 ,description='A vegeterian roll rapped in Rice')
# print(restaurant)
