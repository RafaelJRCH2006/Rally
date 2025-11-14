import json
import os

ARCHIVO = 'registro.json'

def cargar_registros():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_registros(registros):
    with open(ARCHIVO, 'w') as archivo:
        json.dump(registros, archivo, indent=2)

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Agregar registro")
    print("2. Mostrar registros")
    print("3. Buscar registro por nombre")
    print("4. Modificar registros")
    print("5. Salir")
    return input("Opción: ")

def agregar_registro(registros):
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    ciudad = input("Ingrese la ciudad: ")
    registro = {
        'nombre': nombre,
        'edad': edad,
        'ciudad': ciudad
    }
    registros.append(registro)
    guardar_registros(registros)
    print("Registro agregado exitosamente.")

def mostrar_registros(registros):
    if not registros:
        print("No hay registros para mostrar.")
        return
    for idx, registro in enumerate(registros, start=1):
        print(f"{idx}. Nombre: {registro['nombre']}, Edad: {registro['edad']}, Ciudad: {registro['ciudad']}")

def buscar_registro(registros):
    nombre_buscar = input("Ingrese el nombre a buscar: ")
    encontrados = [r for r in registros if r['nombre'].lower() == nombre_buscar.lower()]
    if encontrados:
        for registro in encontrados:
            print(f"Encontrado - Nombre: {registro['nombre']}, Edad: {registro['edad']}, Ciudad: {registro['ciudad']}")
    else:
        print("No se encontraron registros con ese nombre.")

def modificar_registro(registros):
    mostrar_registros(registros)
    indice = int(input("Ingrese el número del registro a modificar: ")) - 1
    if 0 <= indice < len(registros):
        nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
        edad = input("Ingrese la nueva edad (deje en blanco para no cambiar): ")
        ciudad = input("Ingrese la nueva ciudad (deje en blanco para no cambiar): ")
        
        if nombre:
            registros[indice]['nombre'] = nombre
        if edad:
            registros[indice]['edad'] = edad
        if ciudad:
            registros[indice]['ciudad'] = ciudad
        
        guardar_registros(registros)
        print("Registro modificado exitosamente.")
    else:
        print("Índice inválido.")

def main():
    registros = cargar_registros()
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            agregar_registro(registros)
        elif opcion == '2':
            mostrar_registros(registros)
        elif opcion == '3':
            buscar_registro(registros)
        elif opcion == '4':
            modificar_registro(registros)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    
if __name__ == "__main__":
    main()