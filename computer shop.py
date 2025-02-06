class MaxPrice:
    def __init__(self):
        self.__maxprice= 900
    
    def print_price(self):
        print(f"The price of computer is : {self.__maxprice}")
        
    def change_price(self, price):
        self.__maxprice = price
        
c = MaxPrice()
c.print_price()

c.__maxprice = 1500
c.print_price()

c.change_price(1500)
c.print_price()