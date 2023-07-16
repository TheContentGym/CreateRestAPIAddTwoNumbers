from flask import Flask, request, jsonify

# Imports the necessary modules from the Flask framework.
    #Flask is used to create the Flask application,
    #request is used to access the request object,
    # and jsonify is used to convert Python dictionaries to JSON responses.

app = Flask(__name__)

#Creates a new Flask application instance. The __name__ variable is a special variable that represents the name of the current module. By passing it as an argument, Flask knows where to find the resources (templates, static files, etc.) associated with the application.

@app.route('/add', methods=['POST'])
def add_numbers():
#A decorator that specifies the route and HTTP method for the following function. The @app.route('/add', methods=['POST']) decorator defines the /add endpoint that will handle POST requests.
#In the context of REST APIs, decorators are commonly used to define routes and specify the HTTP methods for handling different requests. They provide a way to associate a URL endpoint with a specific function or class that will handle the request.
        
    data = request.get_json()  # Get the JSON data from the request body    

    if 'number1' not in data or 'number2' not in data:
        return jsonify({'error': 'Invalid input. Please provide number1 and number2.'}), 400
    # Checks if the number1 and number2 keys are present in the JSON data. If either of them is missing, it returns a JSON response with an error message and a 400 status code (Bad Request).

    number1 = data['number1']
    number2 = data['number2']
    #Takes input for number1 and number2 through the REST API

    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        return jsonify({'error': 'Invalid input. Both number1 and number2 should be numbers.'}), 400

    result = number1 + number2
    #add the two numbers

    return jsonify({'result': result}), 200


if __name__ == '__main__':
    app.run()