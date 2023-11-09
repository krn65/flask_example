# The Flask class and the render_template function are imported from the flask module.
# Flask is a web application framework. render_template is a Flask function used to render templates.
from flask import Flask, render_template

# An instance of the Flask class is created. This instance will act as the WSGI application.
# The '__name__' argument determines the root path of the application so that Flask knows where to find resources 
# such as templates and static files.
app = Flask(__name__)

# The app.route decorator is used to define a route for the web application's root URL ('/').
# This means that when a web browser requests the root URL, Flask will call the 'home' function.
@app.route('/')
def home():
    # The 'home' function renders an HTML template ('index.html').
    # The render_template function looks for a template with the given name in the 'templates' folder 
    # which should be in the same directory as this script.
    # 'name' is a context variable that is passed to the template. The template can use this variable
    # to display its value, which in this case is the string "Visitor".
    return render_template('index.html', name='Visitor')

# The script only runs the Flask application server if this script is executed as the "main" module.
# If the script is imported as a module into another script, the Flask application server won't run.
if __name__ == '__main__':
    # The app.run method starts the Flask application server.
    # Setting 'debug=True' enables Flask's debugger, so the server will reload itself on code changes,
    # and provide useful error messages if anything goes wrong.
    app.run(debug=True)
