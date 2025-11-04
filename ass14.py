class ShoppingCart():
    def __init__(self):
        self.items = []
    
    def add_item(self, name, aquantity = 1):
        self.items.append((name, aquantity))
    
    def rm_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
    def currentitems(self):
        return self.items
    
    def calculatetotal(self):
        sum = 0
        for item in self.items:
            sum += item[1]
        return sum


kalata = ShoppingCart()
kalata.add_item("Zeti", 4)
kalata.add_item("Kitri", 5)
kalata.add_item("Pomidori", 3)
kalata.add_item("Xaxvi", 2)
kalata.add_item("Puri", 2)
print(kalata.items)
kalata.rm_item("Kitri")
print(kalata.items)
kalata.rm_item("Puri")
print(kalata.currentitems())
print(kalata.calculatetotal())
