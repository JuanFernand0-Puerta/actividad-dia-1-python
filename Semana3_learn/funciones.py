import random
import string

# Nivel Básico
def saludo(nombre):
    return f"Hola, {nombre}! Bienvenido."

def suma(a, b):
    return a + b

def es_par(numero):
    return "Par" if numero % 2 == 0 else "Impar"

def mayor_edad(edad):
    return "Mayor de edad" if edad >= 18 else "Menor de edad"

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def area_triangulo(base, altura):
    return (base * altura) / 2

def mayor_lista(numeros):
    return max(numeros) if numeros else None

def contar_letras(palabra, letra):
    return palabra.lower().count(letra.lower())

# Nivel Intermedio
def filtrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0]

def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def eliminar_duplicados(lista):
    return list(set(lista))

def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero

def contar_vocales(texto):
    return sum(1 for letra in texto.lower() if letra in "aeiou")

def invertir_texto(texto):
    return texto[::-1]

# Nivel Avanzado
def validar_contraseña(contraseña):
    return (
        any(c.isupper() for c in contraseña) and
        any(c.islower() for c in contraseña) and
        any(c.isdigit() for c in contraseña) and
        any(c in string.punctuation for c in contraseña) and
        len(contraseña) >= 8
    )

def lanzar_dado():
    return random.randint(1, 6)

def suma_unicos(lista):
    return sum(num for num in set(lista) if lista.count(num) == 1)

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def composicion(funcion1, funcion2, valor):
    return funcion2(str(funcion1(valor)))  # Corregido para evitar errores de tipo