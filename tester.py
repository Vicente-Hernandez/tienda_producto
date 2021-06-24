class tienda:
    def __init__(self, name):
        self.name = name
        self.productList = []
        
    def add_product(self, new):
        self.productList.append(new)
        return self
    
    def sell_product(self, id):
        self.productList=list(filter(lambda x:x.id!=id,self.productList))
        #self.productList.pop[id]
        #print('Se vendió: ' + str(self.productList[id].name))
    
    def inflation(self, percent_incrase):
        for product in self.productList:
            product.update_price(percent_incrase, True)
        return self
    
    def set_clearance (self, category, percent_discount):
        for product in self.productList:
            if product.category == category:
                product.update_price(percent_discount,False)
        return self
    
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

luchita = tienda('luchita')
arroz = product('arroz', 500, 'granos', 43)
leche = product('leche', 1000, 'lacteos', 29)
fideos = product('fideos', 900, 'pastas', 18)
yogurth = product('yogurth', 50, 'lacteos', 10)
arroz.print_info()
arroz.update_price(0.01, False)
luchita.add_product(arroz).add_product(leche).add_product(fideos).add_product(yogurth)
luchita.sell_product(18)
luchita.inflation(0.3)
luchita.set_clearance('lacteos', 0.02)