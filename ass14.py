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
kalata.add_item("kitri", 5)
kalata.add_item("pmidor", 3)
kalata.add_item("ketesa", 2)
kalata.add_item("saba", 2)
print(kalata.items)
kalata.rm_item("kitri")
print(kalata.items)
kalata.rm_item("saba")
print(kalata.currentitems())
print(kalata.calculatetotal())
