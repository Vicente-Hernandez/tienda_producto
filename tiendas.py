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
            product.price *= (1 + percent_incrase)
        return self
    
    def set_clearance (self, category, percent_discount):
        for product in self.productList:
            if product.category == category:
                product.update_price(percent_discount,False)
        return self

