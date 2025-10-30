class AnalisisAlgoritmos:
    """Implementa búsqueda binaria y recursividad para análisis de datos."""
    
    # Busca un elemento (ej: una parada) en un array ordenado (O(log n)).
    @staticmethod
    def busqueda_binaria(arr, target):
        target = target.lower().strip()
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            current = arr[mid].lower().strip()
            
            if current == target:
                return mid
            elif current < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1

    # Valida recursivamente si dos textos son similares (recursividad).
    @staticmethod
    def validar_recursivo(text1, text2, depth=0):
        if depth > 100: 
            return False 

        clean1 = text1.lower().strip().replace(" ", "")
        clean2 = text2.lower().strip().replace(" ", "")

        if clean1 == clean2:
            return True
        
        if ',' in text1:
            new_text1 = text1.rsplit(',', 1)[0]
            # Caso Recursivo: La función se llama a sí misma
            return AnalisisAlgoritmos.validar_recursivo(new_text1, text2, depth + 1)
            
        return False