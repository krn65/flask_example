# Import the Flask class from the flask module. Flask is a lightweight WSGI web application framework.
from flask import Flask

# Create an instance of the Flask class. '__name__' is a special variable in Python that represents the name of the current module.
# When using a single module, '__name__' is the correct value to use. This lets Flask know where to find other files (like templates).
app = Flask(__name__)

# The app.route decorator is used to register a view function for a given URL rule.
# This tells Flask that when a web browser requests the root URL ('/'), the function below should be called.
@app.route('/')
def hello_world():
    # The function 'hello_world()' is associated with the root URL ('/').
    # When this URL is requested, the text 'Hello, World!' is returned to the browser.
    return 'Hello, World!'

# Another route decorator that tells Flask to call the following function when the '/about' URL is requested.
@app.route('/about')
def about():
    # The function 'about()' is associated with the URL '/about'.
    # When this URL is requested, the text 'About Page' is returned to the web browser.
    return 'About Page'

# The script only runs the Flask application server if this script is executed as the "main" module.
# If the script is imported as a module into another script, the Flask application server won't run.
if __name__ == '__main__':
    # The app.run method starts the Flask application server.
    # Setting 'debug=True' enables Flask's debugger, so the server will reload itself on code changes,
    # and provide useful error messages if anything goes wrong.
    app.run(debug=True)
