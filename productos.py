class product:
    
    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id
        
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price *= (1 + percent_change)
        if is_increased == False:
            self.price *= (1 - percent_change)
        return self
    
    def print_info(self):
        return print(f'El producto consultado es: {self.name} \nCategoria {self.category} \nPrecio es de $ {self.price}')
        return self




