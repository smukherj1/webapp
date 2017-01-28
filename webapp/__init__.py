from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_view():
    return '<html><title>Hello!</title><body><h1>Hello!</h1>Howdy! How ya doin?</body></html>'

if __name__ == '__main__':
    app.run()
