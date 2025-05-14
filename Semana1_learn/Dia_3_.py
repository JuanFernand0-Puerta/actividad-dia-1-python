print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("     GESTIÓN DE BIBLIOTECA     ")
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

biblioteca = {
    '001': {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    '002': {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949}
}

def agregar_libro():
    while True:
        try:
            id_libro = input("Ingrese el ID del libro: ").strip()
            if id_libro in biblioteca:
                print("El libro con este ID ya existe.")
            else:
                break
        except ValueError:
            print("Dato inválido.")

    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()
    
    while True:
        try:
            año = int(input("Ingrese el año de publicación: "))
            break
        except ValueError:
            print("Ingrese un año válido.")

    biblioteca[id_libro] = {'titulo': titulo, 'autor': autor, 'año': año}
    print(f"Libro '{titulo}' agregado correctamente.")

def mostrar_libros():
    print("\nLibros en la biblioteca:")
    for id_libro, detalles in biblioteca.items():
        print(f"ID: {id_libro}, Título: {detalles['titulo']}, Autor: {detalles['autor']}, Año: {detalles['año']}")

def buscar_libro():
    clave = input("Ingrese el ID o título del libro a buscar: ").strip()
    for id_libro, detalles in biblioteca.items():
        if id_libro == clave or detalles['titulo'].lower() == clave.lower():
            print(f"Libro encontrado: {detalles}")
            return
    print("Libro no encontrado.")

def actualizar_libro():
    id_libro = input("Ingrese el ID del libro a actualizar: ").strip()
    if id_libro in biblioteca:
        nuevo_autor = input("Ingrese el nuevo autor (deje vacío si no cambia): ").strip()
        nuevo_año = input("Ingrese el nuevo año de publicación (deje vacío si no cambia): ").strip()
        
        if nuevo_autor:
            biblioteca[id_libro]['autor'] = nuevo_autor
        if nuevo_año.isdigit():
            biblioteca[id_libro]['año'] = int(nuevo_año)

        print(f"Libro '{biblioteca[id_libro]['titulo']}' actualizado correctamente.")
    else:
        print("El libro no existe.")

def eliminar_libro():
    id_libro = input("Ingrese el ID del libro a eliminar: ").strip()
    if id_libro in biblioteca:
        eliminado = biblioteca.pop(id_libro)
        print(f"Libro '{eliminado['titulo']}' eliminado correctamente.")
    else:
        print("El libro no existe.")

mostrar_libros()
agregar_libro()
buscar_libro()
actualizar_libro()
eliminar_libro()
mostrar_libros()
