import re  # Importar el módulo de expresiones regulares
import unittest

def drinkInput(text):
    if text == "":
        return "Mensaje: Entrada vacia."

    # Validate if there are 2 or more consecutive comas
    if re.search(',,+', text):
        return "Mensaje: La entrada no debe contener dos o más comas consecutivas."
    
    if not "," in text:
        return "Mensaje: La entrada debe contener al menos una coma para separar el nombre de los tamaños."

    # Delete blank spaces, and separate them
    parts = text.replace(" ", "").split(",")
    
    # Grab the name
    drinkName = parts[0]

    # Validate the lenght
    if not 2 <= len(drinkName) <= 15 :
        return "Mensaje: El nombre de la bebida debe tener entre 2 y 15 caracteres."
    
    # Validate if it only has alphabetical values
    if not drinkName.isalpha():
        return "Mensaje: El nombre de la bebida debe tener solamente caracteres alfabéticos."
    
    # Grab the sizes
    sizes = parts[1:]

    # Validate amount of sizes
    if not 1 <= len(sizes) <= 5:
        return "Mensaje: La cantidad de tamaños tiene que ser entre 1 y 5."
    
    # Check each size
    sizes_int = []
    for size in sizes:
        # Validations
        if not size.isdigit():
            return "Mensaje: Los tamaños deben ser valores enteros."
        if not 1 <= int(size) <= 48:
            return "Mensaje: Los tamaños deben ser valores dentro del rango de 1 a 48."
        
        sizes_int.append(int(size))
    
    # Validate if they are in order
    if sizes_int != sorted(sizes_int):
        return "Mensaje: Los tamaños deben ingresarse en orden ascendente."
    
    return drinkName, sizes_int

# Tests
class TestDrinkInput(unittest.TestCase):
    def test_nombre_correcto(self):
        self.assertEqual(drinkInput("Cafe,1,2,3"), ("Cafe", [1, 2, 3]))
    
    def test_nombre_demasiado_corto(self):
        self.assertEqual(drinkInput("A,1,2,3"), "Mensaje: El nombre de la bebida debe tener entre 2 y 15 caracteres.")
    
    def test_nombre_demasiado_largo(self):
        self.assertEqual(drinkInput("Abcdefghijklmnop,1,2,3"), "Mensaje: El nombre de la bebida debe tener entre 2 y 15 caracteres.")
    
    def test_nombre_no_alfabetico(self):
        self.assertEqual(drinkInput("123,1,2,3"), "Mensaje: El nombre de la bebida debe tener solamente caracteres alfabéticos.")
    
    def test_comas_consecutivas(self):
        self.assertEqual(drinkInput("Cafe,,1,2,3"), "Mensaje: La entrada no debe contener dos o más comas consecutivas.")
    
    def test_tamanos_desordenados(self):
        self.assertEqual(drinkInput("Cafe,3,1,2"), "Mensaje: Los tamaños deben ingresarse en orden ascendente.")
    
    def test_tamano_fuera_de_rango(self):
        self.assertEqual(drinkInput("Cafe,0,49"), "Mensaje: Los tamaños deben ser valores dentro del rango de 1 a 48.")
    
    def test_cantidad_tamanos_incorrecta(self):
        self.assertEqual(drinkInput("Cafe,1,2,3,4,5,6"), "Mensaje: La cantidad de tamaños tiene que ser entre 1 y 5.")

    def test_tamanos_validos_minimo(self):
        self.assertEqual(drinkInput("Te,1"), ("Te", [1]))
    
    def test_tamanos_validos_maximo(self):
        self.assertEqual(drinkInput("Te,1,2,3,4,48"), ("Te", [1, 2, 3, 4, 48]))
    
    def test_tamanos_repetidos(self):
        self.assertEqual(drinkInput("Te,1,1,2,2,3"), ("Te", [1, 1, 2, 2, 3]))
    
    def test_tamano_minimo(self):
        self.assertEqual(drinkInput("Te,0"), "Mensaje: Los tamaños deben ser valores dentro del rango de 1 a 48.")
    
    def test_tamano_maximo(self):
        self.assertEqual(drinkInput("Te,49"), "Mensaje: Los tamaños deben ser valores dentro del rango de 1 a 48.")
    
    def test_nombre_con_numeros(self):
        self.assertEqual(drinkInput("Te3,1,2,3"), "Mensaje: El nombre de la bebida debe tener solamente caracteres alfabéticos.")
    
    def test_nombre_con_simbolos(self):
        self.assertEqual(drinkInput("Te-Verde,1,2"), "Mensaje: El nombre de la bebida debe tener solamente caracteres alfabéticos.")

    def test_entrada_sin_comas(self):
        self.assertEqual(drinkInput("Cafe"), "Mensaje: La entrada debe contener al menos una coma para separar el nombre de los tamaños.")
    
    def test_entrada_vacia(self):
        self.assertEqual(drinkInput(""), "Mensaje: Entrada vacia.")

    def test_tamano_con_espacio(self):
        self.assertEqual(drinkInput("Cafe, 2 , 3 , 4"), ("Cafe", [2, 3, 4]))
    
    def test_tamano_con_letra(self):
        self.assertEqual(drinkInput("Cafe,2a,3,4"), "Mensaje: Los tamaños deben ser valores enteros.")
    
    def test_tamanos_con_simbolos(self):
        self.assertEqual(drinkInput("Cafe,2,3$,4"), "Mensaje: Los tamaños deben ser valores enteros.")
    
    def test_entrada_con_espacios_extra(self):
        self.assertEqual(drinkInput("  Cafe  , 1 , 2 , 3  "), ("Cafe", [1, 2, 3]))


if __name__ == '__main__':
    unittest.main()