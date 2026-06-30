
import math

def distancia_km(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en km
    R = 6371

    # convertir grados a radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # diferencias
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # fórmula de Haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distancia = R * c
    return distancia


# 📍 Ejemplo (Casa - Tuareg)
lat1, lon1 = 21.183558, -86.897221   # Casa
lat2, lon2 = 21.122047, -86.848346   # Tuareg

print(f"Distancia: {distancia_km(lat1, lon1, lat2, lon2):.2f} km")

