from routes import about , hello_world, app

about()
hello_world()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)