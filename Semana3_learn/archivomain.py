import funciones

# Pruebas de funciones
print(funciones.saludo("Carlos"))
print(funciones.suma(5, 7))
print(funciones.es_par(10))
print(funciones.mayor_edad(17))
print(funciones.celsius_a_fahrenheit(25))
print(funciones.area_triangulo(10, 5))
print(funciones.mayor_lista([3, 7, 1, 9, 2]))
print(funciones.contar_letras("programacion", "o"))

print(funciones.filtrar_pares([1, 2, 3, 4, 5, 6]))
print(funciones.es_palindromo("anilina"))
print(funciones.factorial(5))
print(funciones.eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]))
print(funciones.fizzbuzz(15))
print(funciones.contar_vocales("Python es genial"))
print(funciones.invertir_texto("Hola mundo"))

print(funciones.validar_contraseña("Segur@123"))
print(funciones.lanzar_dado())
print(funciones.suma_unicos([1, 2, 2, 3, 4, 4, 5]))
print(funciones.generar_contraseña(12))

# Composición de funciones
print(funciones.composicion(funciones.celsius_a_fahrenheit, funciones.invertir_texto, 30))