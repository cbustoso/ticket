from flask import Flask, render_template, url_for

app = Flask(__name__)

# CONFIGURACIÓN DEL ARCHIVO MP3 Y LA IMAGEN ALOJADOS EN STATIC
TINI_MP3_FILENAME = "tini_cancion.mp3"  # ¡VERIFICA QUE ESTE NOMBRE COINCIDA CON TU ARCHIVO!
TINI_IMAGE_FILENAME = "image_9f2861.png"

@app.route('/')
def ticket():
    """Renderiza el ticket de concierto de Tini."""
    
    ticket_data = {
        'titulo': "FUTTTURA TOUR",
        'regalo_para': "[NOMBRE DE TU HIJA AQUÍ]",
        'fecha': "12 DE FEBRERO 2026",
        'lugar': "Estadio Nacional, Santiago",
        'sector': "Platea Central (Fila de la suerte)",
        'mensaje': "¡Que la magia de la Navidad se convierta en música! Te amo.",
        'image_filename': TINI_IMAGE_FILENAME,
        'mp3_url': url_for('static', filename=TINI_MP3_FILENAME) # URL dinámica del MP3
    }
    
    return render_template('index.html', **ticket_data)

if __name__ == '__main__':
    # Usaremos el puerto 5001 para evitar el conflicto con el puerto 5000
    app.run(debug=True, host='0.0.0.0', port=5001)