# The flask module is imported. Flask is a web framework for Python that provides functionality for building web applications, 
# including managing requests and responses.
from flask import Flask

# An instance of the Flask class is created. The '__name__' variable in Python represents the name of the current module, 
# which Flask uses to know where to look for templates, static files, and so on.
app = Flask(__name__)

# The app.route decorator is used to tell Flask what URL should trigger the following function.
# When the home ('/') URL is accessed, Flask will execute the 'hello_world' function.
@app.route('/')
def hello_world():
    # This function returns the string 'Hello, World!' as a response.
    return 'Hello, World!'

# The app.route decorator is used again, this time to define a route for the URL '/about'.
@app.route('/about')
def about():
    # This function returns the string 'About Page' when the '/about' URL is accessed.
    return 'About Page'

# A dynamic route is created that accepts a variable 'username'.
# Whatever is passed in the URL at the position '<username>' will be used as the variable.
@app.route('/user/<username>')
def show_user_profile(username):
    # This function receives the 'username' variable from the URL and returns a greeting message 
    # including the passed username. The f-string is used here to format the string with the variable.
    return f'Hello User: {username}!'

# The script only runs the Flask application server if this script is executed as the "main" module.
# If the script is imported as a module into another script, the Flask application server won't run.
if __name__ == '__main__':
    # The app.run method starts the Flask application server.
    # Setting 'debug=True' enables Flask's debugger, so the server will reload itself on code changes,
    # and provide useful error messages if anything goes wrong.
    app.run(debug=True)
