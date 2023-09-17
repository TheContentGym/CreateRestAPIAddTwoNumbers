# Import necessary modules from the Flask framework
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a route using the @app.route decorator to handle GET requests to '/add'
# Decorators like @app.route are used to map URL routes and HTTP methods, making the code into REST APIs.
@app.route('/add', methods=['GET'])
def add_numbers():
    # Retrieve 'number1' and 'number2' from query parameters
    number1 = request.args.get('number1', type=float)
    number2 = request.args.get('number2', type=float)

    # Check if either 'number1' or 'number2' is missing
    if number1 is None or number2 is None:
        # Return a JSON response with an error message and a 400 status code (Bad Request)
        return jsonify({'error': 'Invalid input. Please provide number1 and number2 as query parameters.'}), 400

    # Calculate the result by adding 'number1' and 'number2'
    result = number1 + number2

    # Return a JSON response with the result and a 200 status code (OK)
    return jsonify({'result': result}), 200

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run()
