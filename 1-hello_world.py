# Importing the Flask class from the 'flask' package.
# Flask class is a WSGI application and acts as the central object of your application.
from flask import Flask

# Creating an instance of the Flask class. The first argument is the name of the
# application’s module or package, which is used by Flask to find resources,
# templates, static files, instance folder, etc. '__name__' is a built-in
# variable which evaluates to the name of the current module. This is needed so
# that Flask knows where to look for templates, static files, and so on.
app = Flask(__name__)

# The route() decorator is used to bind a function to a URL. Here, we are defining
# the 'route' for the root URL, which is '/'. This means that when a web browser
# requests the root URL, Flask will invoke the 'hello_world' function below.
@app.route('/')
def hello_world():
    # This function is called when the root URL is accessed. It returns a string,
    # which will be displayed on the client's web browser. The return value can
    # also be more complex, such as an HTML template.
    return 'Hello, World!'

# The script only runs the Flask application server if this script is executed as the "main" module.
# If the script is imported as a module into another script, the Flask application server won't run.
if __name__ == '__main__':
    # The app.run method starts the Flask application server.
    # Setting 'debug=True' enables Flask's debugger, so the server will reload itself on code changes,
    # and provide useful error messages if anything goes wrong.
    app.run(debug=True)
