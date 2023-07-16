Add Two Numbers API

This is a simple Flask API that performs addition of two numbers. It provides an endpoint /add to accept a POST request with JSON data containing number1 and number2 for addition.

Requirements

Python 3.x
Flask (Install using pip install flask)
Installation

Clone the repository or download the code.
Install the required dependencies using the following command:
Copy code
pip install -r requirements.txt
Usage

Run the Flask server by executing the following command:
Copy code
python app.py
This will start the server on http://127.0.0.1:5000.
Make a POST request to the /add endpoint using your preferred method (e.g., curl, Postman, etc.). The request should include the JSON data with number1 and number2 as keys and their respective values.
Example:
bash
Copy code
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "number1": 5,
    "number2": 10
}' \
  http://127.0.0.1:5000/add
The response will be a JSON object with the addition result:
json
Copy code
{
  "result": 15
}
If the JSON data is missing number1 or number2, or if they are not valid numbers, an error response will be returned:
json
Copy code
{
  "error": "Invalid input. Please provide number1 and number2."
}
Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License.
