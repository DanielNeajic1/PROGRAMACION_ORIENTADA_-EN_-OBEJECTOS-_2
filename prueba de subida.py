# main.py

from biblioteca import Libro, Miembro, Biblioteca
from datetime import datetime


def main():
    # Crear una biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(Libro("978-3-16-148410-0", "Cien Años de Soledad", "Gabriel García Márquez", 5))
    biblioteca.agregar_libro(Libro("978-0-7432-7356-5", "El Alquimista", "Paulo Coelho", 3))
    biblioteca.agregar_libro(Libro("978-1-56619-909-4", "1984", "George Orwell", 4))

    # Registrar miembros en la biblioteca
    miembro1 = Miembro(1, "María González", "maria.gonzalez@example.com")
    miembro2 = Miembro(2, "Carlos Pérez", "carlos.perez@example.com")
    biblioteca.registrar_miembro(miembro1)
    biblioteca.registrar_miembro(miembro2)

    # Realizar un préstamo
    fecha_prestamo = datetime.now().date()
    fecha_devolucion = datetime.now().date()
    prestamo = biblioteca.realizar_prestamo("978-3-16-148410-0", 1, fecha_prestamo, fecha_devolucion)

    if prestamo:
        print("Préstamo realizado con éxito:")
        print(prestamo)
    else:
        print("No se pudo realizar el préstamo.")

    # Listar libros disponibles después del préstamo
    print("\nLibros disponibles:")
    for libro in biblioteca.listar_libros_disponibles():
        print(libro)

    # Devolver un libro
    devolucion = biblioteca.devolver_libro("978-3-16-148410-0", 1)

    if devolucion:
        print("\nLibro devuelto con éxito:")
        print(devolucion)
    else:
        print("No se pudo devolver el libro.")

    # Mostrar el estado de la biblioteca
    print("\nEstado de la biblioteca:")
    print(biblioteca)


if __name__ == "__main__":
    main()
