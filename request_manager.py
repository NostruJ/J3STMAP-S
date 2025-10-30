import requests

class RequestManager:
    """Gestiona las llamadas a la Google Directions API."""
    
    # Constructor: Inicializa con la clave de API.
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/directions/json"
        
    # Realiza la solicitud a la API para obtener los datos de la ruta (el grafo resuelto).
    def get_route_data(self, origin, destination, waypoints=None):
        waypoint_str = "|".join(waypoints) if waypoints else None
        
        params = {
            "origin": origin,
            "destination": destination,
            "key": self.api_key,
            "mode": "driving",
            "units": "metric",
        }
        
        if waypoint_str:
            optimize = "true" if len(waypoints) > 1 else "false"
            params["waypoints"] = f"optimize:{optimize}|" + waypoint_str
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data["status"] == "OK":
                return data
            else:
                print(f"❌ Error en la API: {data.get('error_message', data['status'])}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión: {e}")
            return None