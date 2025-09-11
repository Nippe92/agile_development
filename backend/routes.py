from app import app

@app.route('/about')
def about():
    """
    Denna funktion körs när någon besöker /about
    Du kan ha så många routes du vill
    """
    return '<h1>Om-sida</h1><p>Detta är en enkel Flask-app deployad på Render.</p>'