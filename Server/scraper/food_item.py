class Food_Item:
    name = "" # representable name
    price = 0.0 # price in USD
    UPC = 0 # UPC (Universal Product Code)
    size = "" # Serving size
    health_info = [] # Health stats

    def __init__(self, name, price, UPC):
        self.name = name
        self.price = price
        self.UPC = UPC
    
    