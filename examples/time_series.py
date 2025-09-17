from bottle import Bottle, route, run, static_file

app = Bottle() # Explicit app instance

# Define a route for the home page
@app.route('/')
def home():
    return '<h1>Hello from Bottle!</h1><p>This page is being served by a Bottle server.</p>'

@app.route('/static/<filepath:path>')
def server_static(filepath):
    # Note that requests cannot escape (see parents) of root directory
    return static_file(filepath, root='/path/to/your/static/files')


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
