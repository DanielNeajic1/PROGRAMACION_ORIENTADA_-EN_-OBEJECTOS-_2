import os
import subprocess


def mostrar_codigo_y_ejecutar(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())

        # Ejecutar el script
        print("\nEjecutando el script...\n")
        subprocess.run(['python', ruta_script_absoluta])  # Cambia 'python' por 'python3' si es necesario
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer o ejecutar el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'SEMANA 2/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'SEMANA 3/1.3_programacion_poo_semana_3.py',
        '3': 'SEMANA 4/tienda.py',
        '4': 'SEMANA 5/ingresar_empleado.py',
        '5': 'SEMANA 6/Clase Base y Clase Derivada.py',
        '6': 'SEMANA 7/FileManager.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código y ejecutarlo o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo_y_ejecutar(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
