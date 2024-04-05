import unittest

def is_palindrome(value):
    # Itera sobre cada índice en el rango de la longitud de la cadena
    for i in range(len(value)):
        # Comprueba si el carácter en la posición actual no es igual al carácter
        # simétrico opuesto en la cadena
        if value[i] != value[-(i + 1)]:
            # Si los caracteres no son iguales, la cadena no es un palíndromo,
            # por lo que devuelve False y finaliza la función
            return False
    # Si todas las comparaciones fueron iguales para cada par de caracteres opuestos,
    # la cadena es un palíndromo, así que devuelve True
    return True

def obtener_cantidad_de_palabras_palindrome(lista_palabras):
    contador_palindromos = 0
    for palabra in lista_palabras:
        # Eliminar los espacios de la palabra y convertirla a minúsculas
        # elimina comas y guiones de la palabra
        palabra = palabra.replace(",", "").replace("-", "").replace(" ", "").lower()
        # Verificar si la palabra es un palíndromo
        if is_palindrome(palabra):
            # contador_palindromos += 1
            contador_palindromos = contador_palindromos + 1
    return contador_palindromos







class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
			"A man, a plan, a canal - Panama"
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 6)


unittest.main()