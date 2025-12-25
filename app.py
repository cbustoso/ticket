from flask import Flask, render_template

app = Flask(__name__)

# Configuración Global
# Puedes cambiar este link por el de cualquier canción de Tini
SPOTIFY_EMBED_URL = "https://open.spotify.com/embed/playlist/4FxahxBdTnq83BcUiCmJ6X?utm_source=generator"
TINI_IMAGE_FILENAME = "image_9f2861.png"

@app.route('/')
def ticket_laura():
    """Ruta para el ticket de Laura Soto."""
    ticket_data = {
        'titulo': "FUTTTURA TOUR",
        'regalo_para': "Laura Soto",
        'fecha': "12 DE FEBRERO 2026",
        'lugar': "Estadio Nacional, Santiago",
        'sector': "Andes",
        'mensaje': "¡Que la magia de la Navidad se convierta en música! Te amo.",
        'image_filename': TINI_IMAGE_FILENAME,
        'spotify_embed_url': SPOTIFY_EMBED_URL,
        'pdf_filename': 'Laura_Soto.pdf'  # Archivo en static/
    }
    return render_template('index.html', **ticket_data)

@app.route('/inicio')
def ticket_leticia():
    """Ruta para el ticket de Leticia Sandoval."""
    ticket_data = {
        'titulo': "FUTTTURA TOUR",
        'regalo_para': "Leticia Sandoval",
        'fecha': "12 DE FEBRERO 2026",
        'lugar': "Estadio Nacional, Santiago",
        'sector': "Andes",
        'mensaje': "¡Un regalo mágico para una persona mágica! Disfruta el show.",
        'image_filename': TINI_IMAGE_FILENAME,
        'spotify_embed_url': SPOTIFY_EMBED_URL,
        'pdf_filename': 'Leticia_Sandoval.pdf' # Archivo en static/
    }
    return render_template('index.html', **ticket_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')