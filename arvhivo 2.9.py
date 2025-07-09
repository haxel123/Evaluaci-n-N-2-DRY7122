import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "8bc67068-d89a-4e21-ab2c-3abc59f3050b"

def geocodificacion(ubicacion, key):
    while ubicacion == "":
        ubicacion = input("Por favor ingrese la ubicación nuevamente: ")
    
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": ubicacion, "limit": "1", "key": key})
    
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        print(f"Error en la API de geocodificación: {respuesta.status_code}")
        return respuesta.status_code, "null", "null", ubicacion
    
    datos_json = respuesta.json()
    
    if len(datos_json.get("hits", [])) == 0:
        print("No se encontraron resultados para esta ubicación")
        return 404, "null", "null", ubicacion
    
    punto = datos_json["hits"][0]["point"]
    nombre = datos_json["hits"][0]["name"]
    tipo = datos_json["hits"][0].get("osm_value", "desconocido")
    
    pais = datos_json["hits"][0].get("country", "")
    estado = datos_json["hits"][0].get("state", "")
    
    nueva_ubicacion = nombre
    if estado:
        nueva_ubicacion += f", {estado}"
    if pais:
        nueva_ubicacion += f", {pais}"
    
    print(f"Geocodificación exitosa para: {nueva_ubicacion} (Tipo: {tipo})")
    return respuesta.status_code, punto["lat"], punto["lng"], nueva_ubicacion

while True:
    print("\n" + "="*50)
    print("SELECCIÓN DE MEDIO DE TRANSPORTE")
    print("="*50)
    print("Opciones disponibles: Auto, Bicicleta, Caminando")
    print("Escriba 'salir' en cualquier momento para terminar")
    print("="*50)
    
    perfil = input("Seleccione medio de transporte: ").capitalize()
    if perfil.lower() in ["salir", "s", "q"]:
        break
    elif perfil not in ["Auto", "Bicicleta", "Caminando"]:
        perfil = "Auto"
        print("Opción no válida. Usando Auto por defecto.")
    
    print("\n" + "-"*50)
    origen = input("Ubicación de partida: ")
    if origen.lower() in ["salir", "s", "q"]:
        break
        
    estado_geo, lat_origen, lng_origen, nombre_origen = geocodificacion(origen, key)
    if estado_geo != 200:
        print(f"Error geocodificando origen: {nombre_origen}")
        continue
    
    print("\n" + "-"*50)
    destino = input("Ubicación de destino: ")
    if destino.lower() in ["salir", "s", "q"]:
        break
        
    estado_geo, lat_destino, lng_destino, nombre_destino = geocodificacion(destino, key)
    if estado_geo != 200:
        print(f"Error geocodificando destino: {nombre_destino}")
        continue
    
    print("\n" + "="*50)
    print("CALCULANDO RUTA...")
    print("="*50)
    
    # Construir URL para la ruta
    puntos = f"&point={lat_origen},{lng_origen}&point={lat_destino},{lng_destino}"
    url_ruta = route_url + urllib.parse.urlencode({
        "key": key,
        "vehicle": perfil.lower(),
        "locale": "es"
    }) + puntos
    
    respuesta_ruta = requests.get(url_ruta)
    datos_ruta = respuesta_ruta.json()
    
    if respuesta_ruta.status_code != 200:
        print(f"Error en API de rutas: {respuesta_ruta.status_code}")
        print(f"Mensaje: {datos_ruta.get('message', 'Sin detalles')}")
        continue
        
    if "paths" not in datos_ruta or not datos_ruta["paths"]:
        print("No se pudo calcular la ruta. Verifique las ubicaciones.")
        continue
    
    ruta = datos_ruta["paths"][0]
    
    # Calcular distancias y tiempo
    distancia_km = ruta["distance"] / 1000
    distancia_millas = distancia_km * 0.621371
    
    segundos_totales = int(ruta["time"] / 1000)
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60
    
    print("\n" + "="*50)
    print(f"RUTA: {nombre_origen} → {nombre_destino}")
    print(f"Medio: {perfil}")
    print("-"*50)
    print(f"Distancia total: {distancia_km:.1f} km ({distancia_millas:.1f} millas)")
    print(f"Duración estimada: {horas:02d}:{minutos:02d}:{segundos:02d}")
    print("\nINSTRUCCIONES DE VIAJE:")
    
    # Mostrar instrucciones paso a paso
    for i, paso in enumerate(ruta["instructions"], 1):
        distancia_paso = paso["distance"] / 1000
        print(f"{i}. {paso['text']} ({distancia_paso:.1f} km)")
    
    print("="*50)
    print("\n\n")
