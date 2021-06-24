from tiendas import tienda
from productos import product

# importar el marco de prueba de Python 
import unittest
# nuestra "unit"
# esto es lo que estamos ejecutando nuestra prueba en 
# nuestros "unit tests" 
# inicializado creando una clase que hereda de unittest.TestCase 
class IsEvenTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testRise(self):
        arroz = product('arroz', 100, 'cereales', 1)
        leche = product('leche', 200, 'lacteo', 2)
        okmarket = tienda('okmarket')
        test = arroz.update_price(0.0, True)
        resultado = arroz.price
        
        self.assertEqual(
        




    def setUp(self):
        # agrega las tareas setUp 
        print("Comenzando el testeo")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown 
        print("Fin de testeo")
if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas
