from MenuItem import MenuItem

# class Diner(object):

#     STATUSES = ['seated', 'ordering', 'eating', 'paying', 'leaving']

#     def __init__(self, name):
#         self.__name = name
#         self.__order = []
#         self.__status = self.STATUSES[0]
    

#     def __str__(self):
#         return ('Diner {} is currently {}'.format(self.__name, self.__status))

#     __repr__ = __str__

#     def updateStatus(self):
#         for value, key in enumerate(self.STATUSES):
#             if self.STATUSES[4] == self.__status:
#                 print('Customer is done')
#                 break
#             elif self.STATUSES[value] == self.__status:
#                 self.__status = self.STATUSES[value+1]
#                 break

#     def printOrder(self):
#         print('All your order: ', self.__order)

#     def calculateMealCost(self):
#         return sum([item[1] for item in self.__order])



#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, value):
#         self.__name = value

#     @property
#     def order(self):
#         return self.__order

#     @order.setter
#     def order(self, value):
#         self.__order = value
    
#     @property
#     def status(self):
#         return self.__status

#     @status.setter
#     def status(self, value):
#         self.__status = value


class Diner(object):
    STATUS = ["seated", "ordering", "eating", "paying", "leaving"]

    def __init__(self, name):
        self.__name = name
        self.__order = []
        self.__status = self.STATUS[0]

    def __str__(self):
        return 'Diner {p.name} is currently {p.status}\n'.format(p=self)
class Diner(object):
    STATUS = ["seated", "ordering", "eating", "paying", "leaving"]

    def __init__(self, name):
        self.__name = name
        self.__order = []
        self.__status = self.STATUS[0]

    def __str__(self):
        return 'Diner {p.name} is currently {p.status}\n'.format(p=self)

    __repr__ = __str__

    def updateStatus(self):
        for value, key in enumerate(self.STATUS):
            if self.STATUS[4] == self.__status:
                print("Update failed, the Diner is leaving")
                break
            elif self.STATUS[value] == self.__status:
                self.__status = self.STATUS[value + 1]
                break

    def printOrder(self):
        print("Above all, You order the ", self.__order)

    def calculateMealCost(self):
        for value in self.__order:
            return MenuItem[key].price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value