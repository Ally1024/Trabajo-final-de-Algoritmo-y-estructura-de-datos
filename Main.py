# principal.py

import base_de_datos
import ordenamiento_radix
import busqueda_binaria
import time #Importamos la biblioteca de tiempo
import tracemalloc # Importamos la biblioteca para rastrear la memoria

# Variable global para saber cómo está ordenada la lista actualmente
orden_actual = None

def imprimir_registros(registros):
    """Imprime los registros de estudiantes de forma legible."""
    if not registros:
        print("No hay registros para mostrar.")
        return
    print("-" * 50)
    print(f"{'CIF':<15} | {'Edad':<5} | {'Calificación':<12}")
    print("-" * 50)
    for registro in registros:
        print(f"{registro['cif']:<15} | {registro['edad']:<5} | {registro['calificacion']:<12}")
    print("-" * 50)

def buscar_por_cif(registros, cif):
    """Realiza una búsqueda lineal simple por CIF."""
    for registro in registros:
        if registro['cif'].lower() == cif.lower():
            return registro
    return None

def menu_principal():
    """Función principal que ejecuta el menú interactivo."""
    global orden_actual
    
    print("Cargando base de datos de estudiantes...")
    lista_estudiantes = base_de_datos.obtener_registros_estudiantes()
    print(f"¡Base de datos cargada con {len(lista_estudiantes)} registros!")
    print("\n¡Bienvenido al Sistema de Gestión de Notas!")
    
    lista_original = list(lista_estudiantes)

    tracemalloc.start() # -> INICIAMOS EL RASTREO DE MEMORIA

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print(f"Estado actual: Lista {'ordenada por ' + orden_actual if orden_actual else 'desordenada'}")
        print("1. Mostrar primeros 20 registros")
        print("2. Ordenar registros por Calificación")
        print("3. Ordenar registros por Edad")
        print("4. Buscar por Calificación (Búsqueda Binaria)")
        print("5. Buscar por CIF (Búsqueda Lineal)")
        print("6. Restaurar lista original (desordenada)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nMostrando los primeros 20 registros...")
            imprimir_registros(lista_estudiantes[:20])
        
        elif opcion == '2':
            print("\nOrdenando por calificación...")
            # --- Medición de rendimiento ---
            tiempo_inicio = time.perf_counter()
            tracemalloc.clear_traces() # Limpiamos trazas anteriores
            
            ordenamiento_radix.ordenar(lista_estudiantes, clave=lambda x: x['calificacion'])
            
            memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
            tiempo_fin = time.perf_counter()
            # --- Fin de la medición ---
            
            orden_actual = 'calificacion'
            duracion_ms = (tiempo_fin - tiempo_inicio) * 1000
            print(f"✅ ¡Lista ordenada!")
            print(f"   - Tiempo de ejecución: {duracion_ms:.4f} milisegundos.")
            print(f"   - Pico de memoria usado: {memoria_pico / 1024:.4f} KB.")

        elif opcion == '3':
            print("\nOrdenando por edad...")
            # --- Medición de rendimiento ---
            tiempo_inicio = time.perf_counter()
            tracemalloc.clear_traces()
            
            ordenamiento_radix.ordenar(lista_estudiantes, clave=lambda x: x['edad'])
            
            memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
            tiempo_fin = time.perf_counter()
            # --- Fin de la medición ---
            
            orden_actual = 'edad'
            duracion_ms = (tiempo_fin - tiempo_inicio) * 1000
            print(f"✅ ¡Lista ordenada!")
            print(f"   - Tiempo de ejecución: {duracion_ms:.4f} milisegundos.")
            print(f"   - Pico de memoria usado: {memoria_pico / 1024:.4f} KB.")

        elif opcion == '4':
            if orden_actual != 'calificacion':
                print("⚠️  Advertencia: La lista debe estar ordenada por calificación.")
                continue
            
            try:
                nota_a_buscar = int(input("Ingrese la calificación a buscar: "))
                
                # --- Medición de rendimiento ---
                tiempo_inicio = time.perf_counter()
                tracemalloc.clear_traces()

                resultado = busqueda_binaria.buscar(lista_estudiantes, nota_a_buscar, clave=lambda x: x['calificacion'])

                memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
                tiempo_fin = time.perf_counter()
                # --- Fin de la medición ---
                
                duracion_ms = (tiempo_fin - tiempo_inicio) * 1000
                print(f"⏱️ Búsqueda completada.")
                print(f"   - Tiempo de ejecución: {duracion_ms:.4f} milisegundos.")
                print(f"   - Pico de memoria usado: {memoria_pico / 1024:.4f} KB.")

                if resultado:
                    print("\n🎉 ¡Estudiante encontrado!")
                    imprimir_registros([resultado])
                else:
                    print("\n❌ No se encontró un estudiante con esa calificación.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        elif opcion == '5':
            cif_a_buscar = input("Ingrese el CIF a buscar: ")
            
            # --- Medición de rendimiento ---
            tiempo_inicio = time.perf_counter()
            tracemalloc.clear_traces()
            
            resultado = buscar_por_cif(lista_estudiantes, cif_a_buscar)

            memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
            tiempo_fin = time.perf_counter()
            # --- Fin de la medición ---

            duracion_ms = (tiempo_fin - tiempo_inicio) * 1000
            print(f"⏱️ Búsqueda completada.")
            print(f"   - Tiempo de ejecución: {duracion_ms:.4f} milisegundos.")
            print(f"   - Pico de memoria usado: {memoria_pico / 1024:.4f} KB.")

            if resultado:
                print("\n🎉 ¡Estudiante encontrado!")
                imprimir_registros([resultado])
            else:
                print("\n❌ No se encontró un estudiante con ese CIF.")
        
        elif opcion == '6':
            lista_estudiantes = list(lista_original)
            orden_actual = None
            print("\n🔄 Lista restaurada a su estado original desordenado.")

        elif opcion == '7':
            tracemalloc.stop() # -> DETENEMOS EL RASTREO ANTES DE SALIR
            print("\nGracias por usar el sistema. ¡Hasta pronto! 👋")
            break
        
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()