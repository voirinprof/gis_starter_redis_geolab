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

# function to search for addresses in Redis
def addressSearch(query):

    # Use the zscan command to iterate over the sorted set index
    matches = []
    for match in client.zscan_iter("index_locations"):
        match_str = match[0]
        if match_str.startswith(query):
            matches.append(match_str)
    suggestions = []
    for match in matches:
        adresse = match
        coordonnees = client.geopos("locations", adresse)
        if coordonnees:
            lat = coordonnees[0][1]
            lon = coordonnees[0][0]
            suggestions.append({"display_name": adresse, "lat": lat, "lon": lon})

    return suggestions

# Exemple d’utilisation
if __name__ == "__main__":
    points = addressSearch('Point #1')
    print(points)