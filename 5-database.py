# Import the Flask class to use for our application and the SQLAlchemy class for ORM (Object-Relational Mapping).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the Flask class. This is our WSGI application.
app = Flask(__name__)

# Set the SQLAlchemy database URI for Flask application configuration.
# Here it is configured to use a SQLite database that resides in memory.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

# Disables the Flask-SQLAlchemy event system, which can lead to significant overhead if not needed.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an SQLAlchemy object, which is our ORM to interact with the database. 
# This object will be used to handle database sessions and operations.
db = SQLAlchemy(app)

# Define a User model by inheriting from db.Model, provided by SQLAlchemy.
# This model will map to a table in our database.
class User(db.Model):
    # Define the columns for the User table
    id = db.Column(db.Integer, primary_key=True)  # An integer ID, set as the primary key.
    username = db.Column(db.String(80), unique=True, nullable=False)  # A string column for the username, which is unique and non-nullable.

    # Define a representation method that will define how instances of this model will be printed.
    def __repr__(self):
        return f'<User {self.username}>'

# Function to create and configure the Flask app.
def create_app():
    with app.app_context():
        # Create all tables associated with the models defined using the db.Model class.
        # In this case, it will create a User table in the database.
        db.create_all()
    return app  # Return the configured Flask app.

# Define a route to add a new user to the database.
@app.route('/add_user/<username>')
def add_user(username):
    user = User(username=username)  # Create an instance of the User model.
    db.session.add(user)  # Add the user instance to the database session.
    db.session.commit()   # Commit the session to the database to save our new user.
    return f"Added new user {username}"  # Return a success message.

# Define a route to list all users stored in the database.
@app.route('/users')
def list_users():
    users = User.query.all()  # Query the database for all users.
    # Generate a string that lists all usernames, separated by line breaks.
    return '<br>'.join([user.username for user in users])

# The application is only run if the script is executed directly.
if __name__ == '__main__':
    app = create_app()  # Call the create_app function to configure and get our Flask application.
    app.run(debug=True)  # Run the Flask application with debugging enabled.
