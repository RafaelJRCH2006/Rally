import json
import os

ARCHIVO = 'registro.json'

def limpiar_consola():
    """Limpia la consola según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_registros():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_registros(registros):
    with open(ARCHIVO, 'w') as archivo:
        json.dump(registros, archivo, indent=2)

def mostrar_menu():
    print("\n" + "="*40)
    print("    SISTEMA DE REGISTRO")
    print("="*40)
    print("1. Agregar registro")
    print("2. Mostrar registros")
    print("3. Buscar registro por nombre")
    print("4. Modificar registros")
    print("5. Salir")
    print("="*40)
    return input("Opción: ")

def agregar_registro(registros):
    limpiar_consola()
    print("\n--- AGREGAR REGISTRO ---")
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
    print("\n✓ Registro agregado exitosamente.")
    input("\nPresione Enter para continuar...")

def mostrar_registros(registros):
    limpiar_consola()
    print("\n--- REGISTROS ---")
    if not registros:
        print("No hay registros para mostrar.")
    else:
        for idx, registro in enumerate(registros, start=1):
            print(f"{idx}. Nombre: {registro['nombre']}, Edad: {registro['edad']}, Ciudad: {registro['ciudad']}")
    input("\nPresione Enter para continuar...")

def buscar_registro(registros):
    limpiar_consola()
    print("\n--- BUSCAR REGISTRO ---")
    nombre_buscar = input("Ingrese el nombre a buscar: ")
    encontrados = [r for r in registros if r['nombre'].lower() == nombre_buscar.lower()]
    if encontrados:
        print("\nResultados encontrados:")
        for registro in encontrados:
            print(f"• Nombre: {registro['nombre']}, Edad: {registro['edad']}, Ciudad: {registro['ciudad']}")
    else:
        print("\n✗ No se encontraron registros con ese nombre.")
    input("\nPresione Enter para continuar...")

def modificar_registro(registros):
    limpiar_consola()
    print("\n--- MODIFICAR REGISTRO ---")
    if not registros:
        print("No hay registros para modificar.")
        input("\nPresione Enter para continuar...")
        return
    
    mostrar_registros_sin_pausa(registros)
    try:
        indice = int(input("\nIngrese el número del registro a modificar: ")) - 1
        if 0 <= indice < len(registros):
            print(f"\nRegistro actual: {registros[indice]}")
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
            print("\n✓ Registro modificado exitosamente.")
        else:
            print("\n✗ Índice inválido.")
    except ValueError:
        print("\n✗ Debe ingresar un número válido.")
    
    input("\nPresione Enter para continuar...")

def mostrar_registros_sin_pausa(registros):
    """Muestra registros sin pausa para usar en otras funciones"""
    if not registros:
        print("No hay registros para mostrar.")
        return
    for idx, registro in enumerate(registros, start=1):
        print(f"{idx}. Nombre: {registro['nombre']}, Edad: {registro['edad']}, Ciudad: {registro['ciudad']}")

def main():
    registros = cargar_registros()
    limpiar_consola()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            agregar_registro(registros)
            limpiar_consola()
        elif opcion == '2':
            mostrar_registros(registros)
            limpiar_consola()
        elif opcion == '3':
            buscar_registro(registros)
            limpiar_consola()
        elif opcion == '4':
            modificar_registro(registros)
            limpiar_consola()
        elif opcion == '5':
            limpiar_consola()
            print("\n¡Hasta luego!")
            break
        else:
            limpiar_consola()
            print("\n✗ Opción inválida. Intente nuevamente.")
    
if __name__ == "__main__":
    main()