class Order :
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,order2):
        if (self.price > order2.price):
            a="price of",self.item ,"is greater than",order2.item
            return a
        else:
            print("price of",self.item , "is less than",order2.item)

order1 = Order("chips",10)
order2 = Order("noodles",20)
print(order1>order2)
