import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Cargar variables de entorno
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Configura las credenciales de Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Obtener las canciones más populares del artista
artist_id = "4gzpq5DPGxSnKTe4SA8HAU"  # Coldplay
response = sp.artist_top_tracks(artist_id)

if response:
    tracks = response["tracks"]
    track_info = []

    for track in tracks:
        name = track["name"]
        popularity = track["popularity"]
        duration_ms = track["duration_ms"]
        duration_min = round(duration_ms / 60000, 2)  # Convertir a minutos

        track_info.append({
            "name": name,
            "popularity": popularity,
            "duration_min": duration_min
        })


    for track in track_info:
        print(f"🎵 {track['name']} - Popularidad: {track['popularity']} - Duración: {track['duration_min']} min")

    # Convertir a DataFrame
    df = pd.DataFrame(track_info)
   

    # Ordenar por popularidad en orden decreciente
    df_sorted = df.sort_values(by="popularity", ascending=False)

    # Imprimir el top 3 de canciones más populares
    print(df_sorted.head(3))

    # Graficar el scatter plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="duration_min", y="popularity", hue="name", palette="tab10", s=100)

    # Etiquetas y título
    plt.xlabel("Duración (minutos)")
    plt.ylabel("Popularidad")
    plt.title("Relación entre Duración y Popularidad de Canciones")
    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")  # Mueve la leyenda afuera
    plt.grid(True)

    # Guardar el gráfico como imagen
    plt.savefig('grafico.png')  # Guarda el gráfico en un archivo

    # Mostrar el gráfico en la pantalla
    plt.show()

print("Parece que no existe correlación entre la duración y la popularidad de la canción")
