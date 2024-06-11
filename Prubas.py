# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a un valor usando su clave
print("Nombre:", mi_diccionario["nombre"])  # Salida: Nombre: Juan
print("Edad:", mi_diccionario["edad"])      # Salida: Edad: 30

# Añadir un nuevo par clave-valor
mi_diccionario["profesión"] = "Ingeniero"
print("Profesión:", mi_diccionario["profesión"])  # Salida: Profesión: Ingeniero

# Modificar un valor existente
mi_diccionario["edad"] = 31
print("Edad actualizada:", mi_diccionario["edad"])  # Salida: Edad actualizada: 31

# Eliminar un par clave-valor
del mi_diccionario["ciudad"]
print("Diccionario después de eliminar 'ciudad':", mi_diccionario)

# Iterar sobre los elementos del diccionario
for clave, valor in mi_diccionario.items():
    print(clave, ":", valor)
