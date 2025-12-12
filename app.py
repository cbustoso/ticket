from flask import Flask, render_template, url_for

app = Flask(__name__)

# URL DE INSERCIÓN DE SPOTIFY SUMINISTRADA POR EL USUARIO
# ¡SE AÑADE EL PARÁMETRO ?autoplay=1 AQUÍ!
SPOTIFY_EMBED_URL = "https://open.spotify.com/embed/playlist/4FxahxBdTnq83BcUiCmJ6X?utm_source=generator?autoplay=1" 
TINI_IMAGE_FILENAME = "image_9f2861.png"

@app.route('/')
def ticket():
    """Renderiza el ticket de concierto de Tini."""
    
    ticket_data = {
        'titulo': "FUTTTURA TOUR",
        'regalo_para': "Laura Soto",
        'fecha': "12 DE FEBRERO 2026",
        'lugar': "Estadio Nacional, Santiago",
        'sector': "Andes",
        'mensaje': "¡Que la magia de la Navidad se convierta en música! Te quiero Toto.",
        'image_filename': TINI_IMAGE_FILENAME,
        'spotify_embed_url': SPOTIFY_EMBED_URL  # Variable para el iframe
    }
    
    return render_template('index.html', **ticket_data)

if __name__ == '__main__':
    # Usaremos el puerto 5001
    app.run(debug=True, host='0.0.0.0')