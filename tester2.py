from tiendas import tienda
from productos import product

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
