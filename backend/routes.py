from  Flask import flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Denna funktion körs när någon besöker din hemsidas startsida
    @app.route('/') dekoratören betyder att denna funktion hanterar förfrågningar till rot-URL:en
    """
    return '<h1>Hello, World!</h1>'


@app.route('/about')
def about():
    """
    Denna funktion körs när någon besöker /about
    Du kan ha så många routes du vill
    """
    return '<h1>Om-sida</h1><p>Detta är en enkel Flask-app deployad på Render.</p>'