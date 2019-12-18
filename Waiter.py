from Menu import Menu
from Diner import Diner

class Waiter(object):
    def __init__(self, Menu):
        self._diners = []
        self._menu = Menu

    def addDiners(self, Diner):
        self._diners.append(Diner)

    def getNumDiners(self):
        return len(self._diners)

    def printDinerStatuses(self):
        for value, key in enumerate(self._diners):
            print('Diners {} is {}'.format(self._diners[value].name, self._diners[value].status))

    def takeOrders(self):
        for value, key in enumerate(self._diners):
            if key.status == 'ordering':
                for menuValue, menuKey in enumerate(self._menu.MENU_ITEM_TYPES):
                    self._menu.printMenuItemsByType(menuKey)
                    myOrder = int(input("Please choose your order(use num):"))
                    self._diners[value].order.append(self._menu.getMenuItem(menuKey, myOrder - 1).name)
                    self._diners[value].printOrder()

    def ringUpDiners(self):
        for value, key in enumerate(self._diners):
            if key.status == 'paying':
                print(self._diners[value].calculateMealCost())

    def removeDoneDiners(self):
        for value, key in enumerate(self._diners):
            if key.status == 'leaving':
                print('{} thank you'.format(self._diners[value].name))
                self._diners.pop(value)

    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for value, key in enumerate(self._diners):
            self._diners[value].updateStatus()