import requests
import tkinter as tk


def get_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    api_url = f"https://api.vagalume.com.br/search.php?art={artist}&mus={song}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        lyrics = data['mus'][0]['text']
        display_lyrics(lyrics)
    else:
        result_label.config(text="Letra não encontrada")

def display_lyrics(lyrics):
    result_text.delete(1.0, "end")  # Limpa o conteúdo anterior
    result_text.insert(tk.END, lyrics)

app = tk.Tk()
app.title("Busca de Letras de Músicas")

artist_label = tk.Label(app, text="Artista:")
artist_label.pack()

artist_entry = tk.Entry(app)
artist_entry.pack()

song_label = tk.Label(app, text="Música:")
song_label.pack()

song_entry = tk.Entry(app)
song_entry.pack()

search_button = tk.Button(app, text="Buscar Letra", command=get_lyrics)
search_button.pack()

result_text = tk.Text(app, height=10, width=60)
result_text.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
