import csv

from MenuItem import MenuItem

class Menu(object):
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def __init__(self, filename):
        self.__menuItemDictionary = {}
        for t in self.MENU_ITEM_TYPES:
            self.__menuItemDictionary[t] = []
        with open(filename) as f:
            reader = list(csv.reader(f))
            for row in reader:
                menuItem = MenuItem(row[0], row[1], row[2], row[3])
                self.__menuItemDictionary[menuItem.types].append(menuItem)

    def getMenuItem(self, types, index):
        for key in self.__menuItemDictionary:
            if key == types:
                myMenuItem = self.__menuItemDictionary[key][index]
        return myMenuItem

    def printMenuItemsByType(self, types):
        print(types, ':')
        for i, v in enumerate(self.__menuItemDictionary[types]):
            print("#", i + 1, v)

    def getNumMenuItemsByType(self, types):
        return len(self.__menuItemDictionary[types])