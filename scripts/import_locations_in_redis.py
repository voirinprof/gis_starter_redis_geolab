import random
import os
import redis

# Récupérer les variables d'environnement
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Connexion à Redis
try:
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    print("Connexion à Redis réussie !")
except redis.ConnectionError as e:
    print(f"Erreur de connexion à Redis : {e}")
    exit(1)

def generate_points(n=100, lat_range=(45.0, 46.0), lon_range=(5.0, 6.0)):
    points = []
    for i in range(n):
        lat = round(random.uniform(*lat_range), 6)
        lon = round(random.uniform(*lon_range), 6)
        text = f"Point #{i+1} near ({lat}, {lon})"
        points.append({
            "latitude": lat,
            "longitude": lon,
            "description": text
        })
    return points

# Exemple d’utilisation
if __name__ == "__main__":
    points = generate_points(n=5)
    for p in points:
        text = p['description']
        client.geoadd("locations", (p['longitude'], p['latitude'], text))
        # Ajoutez également l'adresse à un ensemble trié pour l'index
        client.zadd("index_locations", {text: 1})
