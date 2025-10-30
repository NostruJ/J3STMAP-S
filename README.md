# 📚 DOCUMENTACIÓN DEL DESARROLLO - PLANIFICADOR DE RUTAS AVANZADO

## 🎯 Objetivo del Proyecto

Desarrollar un sistema de backend en Python para calcular rutas óptimas utilizando la **Google Maps Directions API**. El proyecto está diseñado para demostrar la **Programación Orientada a Objetos (POO)** y la implementación de algoritmos clave: **Recursividad** (para validación) y **Búsqueda Binaria** (para análisis de paradas).

---

## 🏗️ Arquitectura y Estructura Modular

El proyecto utiliza un diseño modular, separando las responsabilidades en archivos específicos para la gestión del servicio, la estructura de datos y los algoritmos.

### Estructura de Archivos

proyecto/
├── request_manager.py      # Módulo de Comunicación (REQUEST)
├── grafo_manager.py        # Módulo de Estructura de Datos (GRAFO)
├── analisis_algoritmos.py  # Módulo de Algoritmos (BÚSQUEDA BINARIA / RECURSIVIDAD)
└── main.py                 # Interfaz de Usuario y Controlador (MAIN / MENÚ)

---

## 📋 Módulos y Funcionamiento Detallado

### Módulo 1: 🌐 request_manager.py (Manejo de Solicitudes)

**Propósito:** Encargado exclusivo de la comunicación externa.

| Componente | Función Detallada |
| :--- | :--- |
| **Clase `RequestManager`** | Encapsula el código para interactuar con la Google Directions API. |
| **Función `get_route_data`** | **Núcleo del REQUEST:** Construye los parámetros (Origen, Destino, Paradas, clave API). Envía la petición HTTP GET. La API ejecuta el algoritmo de grafo y devuelve el **JSON del Grafo Resuelto** (la ruta óptima). |

### Módulo 2: 🗺️ grafo_manager.py (Gestor de Rutas / Grafo)

**Propósito:** Interpretar y estructurar el resultado de la ruta.

| Componente | Función Detallada |
| :--- | :--- |
| **Clase `GrafoManager`** | Utiliza la instancia de `RequestManager` (Composición). Gestiona la estructura de la ruta. |
| **Función `generar_ruta`** | Almacena el JSON de la API en `self.last_route_data`. Este JSON representa la **solución del Grafo Dirigido** (el camino más corto) que conecta los puntos de la ruta. |
| **Función `get_route_summary`** | Analiza el Grafo Resuelto. Itera sobre los segmentos de la ruta (`route["legs"]`) para sumar las distancias y duraciones totales y proporcionar las métricas clave. |

### Módulo 3: 🔬 analisis_algoritmos.py (Algoritmos Avanzados)

**Propósito:** Demostrar la aplicación de algoritmos clásicos de forma modular.

| Componente | Algoritmo y Función Detallada |
| :--- | :--- |
| **Recursividad** | **`validar_recursivo(text1, text2)`:** Aplica la **Recursividad** para la validación. Compara Origen y Destino, llamándose a sí misma para limpiar y comparar las ubicaciones hasta un **Caso Base**. |
| **Búsqueda Binaria** | **`busqueda_binaria(arr, target)`:** Implementación **iterativa** del algoritmo (O(log n)). Se usa para buscar una parada específica dentro de una lista de paradas **ordenada**. |

### Módulo 4: 🖥️ main.py (Menú Principal / Controlador)

**Propósito:** Ensamblar los módulos y gestionar la interacción con el usuario.

| Función | Funcionamiento Detallado y Control de Datos |
| :--- | :--- |
| **Variable Global** | **`last_waypoints`:** Almacena las paradas de la última ruta calculada. Esto garantiza la **persistencia de datos** para la Opción 2. |
| **`calcular_ruta` (Opción 1)** | 1. **Validación:** Llama a la función **recursiva**. 2. **Persistencia:** Guarda las paradas ingresadas en `last_waypoints`. 3. Llama al `GrafoManager` para la solicitud. |
| **`demostrar_busqueda_binaria` (Opción 2)** | 1. **Control:** Utiliza `last_waypoints` para asegurar que solo se usan los datos recientes. 2. **Pre-requisito:** **Ordena** la lista de paradas. 3. Llama a la función de **Búsqueda Binaria** para el análisis. |

---