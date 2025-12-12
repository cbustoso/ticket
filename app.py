from flask import Flask, render_template, url_for

app = Flask(__name__)

# URL DE INSERCIÓN DE SPOTIFY (FRAGMENTO CORTO)
# Si deseas cambiar la canción, reemplaza el "4" por el ID de la canción o playlist de Spotify
SPOTIFY_EMBED_URL = "https://open.spotify.com/embed/playlist/4FxahxBdTnq83BcUiCmJ6X?utm_source=generator"

TINI_IMAGE_FILENAME = "image_9f2861.png"

@app.route('/')
def ticket():
    """Renderiza el ticket de concierto de Tini."""
    
    # DATOS EDITABLES DEL TICKET
    ticket_data = {
        'titulo': "FUTTTURA TOUR",
        'regalo_para': "Laura Soto", # <--- ¡CÁMBIALO POR EL NOMBRE DE TU HIJA!
        'fecha': "12 DE FEBRERO 2026",
        'lugar': "Estadio Nacional, Santiago",
        'sector': "Platea Central (Fila de la suerte)",
        'mensaje': "¡Que la magia de la Navidad se convierta en música! Te amo.",
        
        # DATOS TÉCNICOS
        'image_filename': TINI_IMAGE_FILENAME,
        'spotify_embed_url': SPOTIFY_EMBED_URL
    }
    
    return render_template('index.html', **ticket_data)

if __name__ == '__main__':
    # Usamos el puerto 5001 para desarrollo local
    app.run(debug=True, host='0.0.0.0')