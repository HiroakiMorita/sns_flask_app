from flaskr import create_app

app = create_app()

@app.route('/')
def index():
    return "Hello world!!"

if __name__ == '__main__':
    app.run(debug=True)