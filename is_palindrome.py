import unittest


def is_palindrome(value):
    # Itera sobre cada índice en el rango de la longitud de la cadena
    for i in range(len(value)):
        # Imprime los caracteres que se están comparando en esta iteración
        # En el ultimo test donde se pone "hola" imprime solo h y a, al no ser iguales corta ahi
        print("Comparando:", value[i], "y", value[-(i + 1)])
        
        # Comprueba si el carácter en la posición actual no es igual al carácter
        # simétrico opuesto en la cadena
        if value[i] != value[-(i + 1)]:
            # Si los caracteres no son iguales, la cadena no es un palíndromo,
            # por lo que devuelve False y finaliza la función
            return False
    
    # Si todas las comparaciones fueron iguales para cada par de caracteres opuestos,
    # la cadena es un palíndromo, así que devuelve True
    return True

        



class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = "a"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = "ala"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = "neuquen"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = "hola"
        result = is_palindrome(input)
        self.assertFalse(result)


unittest.main()
