class Fruits:
    nutrients="vitamins"
    def __init__(self,name,color,taste,price):
        self.name=name
        self.color=color
        self.taste=taste
        self.price=price
    
    def flavour(self):
        return f"A {self.name} is {self.taste}"
    def market_sales(self):
        return f"The market sells {self.name}s at {self.price}"
    def description(self):
        return f"{self.name} are {self.color} and they usually taste {self.taste}"