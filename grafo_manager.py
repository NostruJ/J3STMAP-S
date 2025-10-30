from request_manager import RequestManager

class GrafoManager:
    """Gestiona la estructura de la ruta y calcula las métricas."""
    
    # Constructor: Inicializa el gestor de peticiones.
    def __init__(self, api_key):
        self.request_manager = RequestManager(api_key)
        self.last_route_data = None
        
    # Calcula y almacena la ruta más óptima (Grafo Resuelto).
    def generar_ruta(self, origin, destination, waypoints=None):
        data = self.request_manager.get_route_data(origin, destination, waypoints)
        self.last_route_data = data
        return data

    # Devuelve un resumen de la distancia y duración total de la ruta.
    def get_route_summary(self):
        if not self.last_route_data or not self.last_route_data["routes"]:
            return "No hay ruta calculada."

        route = self.last_route_data["routes"][0]
        total_distance = 0
        total_duration = 0

        for leg in route["legs"]:
            total_distance += leg["distance"]["value"]
            total_duration += leg["duration"]["value"]

        distance_km = total_distance / 1000
        duration_hours = total_duration / 3600
        
        summary = {
            "origin": route["legs"][0]["start_address"],
            "destination": route["legs"][-1]["end_address"],
            "distance_km": f"{distance_km:.2f}",
            "duration_hours": f"{duration_hours:.2f}",
            "status": "OK"
        }
        return summary