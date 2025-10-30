from grafo_manager import GrafoManager
from analisis_algoritmos import AnalisisAlgoritmos

API_KEY = "PON ACA TU KEY PARA PODER USAR EL PROGRAMA" 

# Variable global para almacenar las últimas paradas
last_waypoints = [] 

# Función principal que ejecuta el menú interactivo.
def menu_principal():
    grafo_manager = GrafoManager(API_KEY)
    
    global last_waypoints
    
    while True:
        print("\n=============================================")
        print("         🧭 MENÚ PLANIFICADOR DE RUTAS      ")
        print("=============================================")
        print("1. 🔍 Calcular Ruta (Grafo Dinámico)")
        print("2. 🕵️ Demostrar Búsqueda Binaria en Paradas")
        print("3. 🚪 Salir")
        print("=============================================")
        
        choice = input("Selecciona una opción: ")
        
        if choice == '1':
            calcular_ruta(grafo_manager)
        elif choice == '2':
            demostrar_busqueda_binaria(last_waypoints)
        elif choice == '3':
            print("👋 Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

# Maneja la opción de cálculo de ruta y guarda las paradas.
def calcular_ruta(manager):
    global last_waypoints 
    
    origin = input("Ingresa Origen: ")
    destination = input("Ingresa Destino: ")
    
    # Uso de la recursividad para validar la entrada.
    if AnalisisAlgoritmos.validar_recursivo(origin, destination):
         print("\n❌ Validación Fallida (Recursividad): Origen y Destino son muy similares.")
         last_waypoints = [] 
         return
    
    waypoints_input = input("Ingresa Paradas (separadas por coma, ej: Honda, Medellín): ")
    waypoints = [wp.strip() for wp in waypoints_input.split(',') if wp.strip()]

    last_waypoints = waypoints 
    
    data = manager.generar_ruta(origin, destination, waypoints)
    
    if data:
        summary = manager.get_route_summary()
        print("\n--- ✅ Ruta Óptima Calculada ---")
        print(f"Ruta: {summary['origin']} -> {summary['destination']}")
        print(f"Distancia Total: {summary['distance_km']} km")
        print(f"Duración Estimada: {summary['duration_hours']} horas")
        print("---------------------------------")
    else:
        last_waypoints = []

# Maneja la opción de demostración de Búsqueda Binaria.
def demostrar_busqueda_binaria(current_waypoints):
    
    if not current_waypoints:
        print("\n⚠️ No se han ingresado paradas en la Opción 1.")
        return
    
    paradas_ordenadas = sorted(current_waypoints)
    
    print("\n--- 🕵️ Demostración de Búsqueda Binaria ---")
    print(f"Paradas a analizar (ordenadas): {paradas_ordenadas}")
    
    search_term = input("Ingresa la parada a buscar: ")
    
    # Llamada al método estático de Búsqueda Binaria.
    index = AnalisisAlgoritmos.busqueda_binaria(paradas_ordenadas, search_term)
    
    if index != -1:
        print(f"✅ Éxito: '{search_term}' encontrado en el índice {index}.")
    else:
        print(f"❌ Fallo: '{search_term}' no se encuentra en la lista.")


if __name__ == "__main__":
    menu_principal()