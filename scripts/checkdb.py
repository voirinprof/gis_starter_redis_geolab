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

# Exemple d'opérations
def main():
    # Définir une clé-valeur
    client.set("example_key", "Hello, Redis!")
    
    # Récupérer la valeur
    value = client.get("example_key")
    print(f"Valeur de 'example_key' : {value}")
    
    # Ajouter des éléments à une liste
    client.rpush("example_list", "item1")
    client.rpush("example_list", "item2")
    
    # Récupérer la liste
    items = client.lrange("example_list", 0, -1)
    print(f"Contenu de 'example_list' : {items}")

if __name__ == "__main__":
    main()