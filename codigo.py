import requests

def obtener_ruta():
    API_KEY = "8bc67068-d89a-4e21-ab2c-3abc59f3050b"  # ¡Obtén una en graphhopper.com!
    url = "https://graphhopper.com/api/1/route"
    
    print("\n" + "="*50)
    print("CALCULADOR DE RUTAS CHILE-ARGENTINA")
    print("="*50)
    
    # Solicitar datos al usuario
    origen = input("\nCiudad de Origen en Chile: ")
    if origen.lower() == 's':
        return False
    
    destino = input("Ciudad de Destino en Argentina: ")
    if destino.lower() == 's':
        return False
    
    print("\nMedios de transporte disponibles:")
    print("1. Auto (car)")
    print("2. Bicicleta (bike)")
    print("3. A pie (foot)")
    transporte = input("Elija medio de transporte (1-3): ")
    
    # Mapear opción a valor de API
    vehiculos = {'1': 'car', '2': 'bike', '3': 'foot'}
    vehiculo = vehiculos.get(transporte, 'car')
    
    # Parámetros para la API
    params = {
        "point": [f"{origen}, Chile", f"{destino}, Argentina"],
        "vehicle": vehiculo,
        "locale": "es",
        "key": API_KEY,
        "instructions": True
    }
    
    try:
        # Hacer petición a la API
        response = requests.get(url, params=params)
        data = response.json()
        
        if "paths" not in data or not data["paths"]:
            print("\nError: No se pudo calcular la ruta. Verifique los nombres de las ciudades.")
            return True
        
        # Obtener datos de la primera ruta
        ruta = data["paths"][0]
        distancia_km = ruta["distance"] / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_min = ruta["time"] / 60000
        
        # Mostrar resultados
        print("\n" + "="*50)
        print(f"RUTA: {origen.capitalize()} (Chile) → {destino.capitalize()} (Argentina)")
        print(f"Medio: {'Auto' if vehiculo == 'car' else 'Bicicleta' if vehiculo == 'bike' else 'A pie'}")
        print("-"*50)
        print(f"Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
        print(f"Duración estimada: {duracion_min:.1f} minutos")
        
        # Mostrar narrativa del viaje
        print("\nNARRATIVA DEL VIAJE:")
        for i, paso in enumerate(ruta["instructions"], 1):
            distancia_paso = paso["distance"] / 1000
            print(f"{i}. {paso['text']} ({distancia_paso:.1f} km)")
        
        print("="*50)
        return True
    
    except Exception as e:
        print(f"\nError: {str(e)}")
        return True

def main():
    print("Bienvenido al Calculador de Rutas Chile-Argentina")
    print("Presione 's' en cualquier momento para salir\n")
    
    while True:
        if not obtener_ruta():
            print("\n¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()



#8bc67068-d89a-4e21-ab2c-3abc59f3050b
"https://graphhopper.com/api/1/route"

import requests

def calcular_ruta():
    # Usa la API Key, NO tu contraseña
    API_KEY = "a123456b-7890-cdef-1234-56789abcdef0"  # 👈 Key de ejemplo
    
    url = "https://graphhopper.com/api/1/route"
    
    # ... resto del código igual ...
    params = {
        "point": [f"{origen}, Chile", f"{destino}, Argentina"],
        "vehicle": vehiculo,
        "locale": "es",
        "key": API_KEY,  # 👈 Aquí solo va la API Key
        "instructions": True
    }
