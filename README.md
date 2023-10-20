# When a technical writer tries to document this REST API:

Ravi Desai is a young technical writer who is tasked with updating the REST API documentation for Calculus Cloud (This REST API). Calculus Cloud is a simple solution that lets clients add two numbers. Ravi is clueless about where to start, but his manager helps him get in touch with the developer Bharat Iyer. Bharat explains that the documentation is in a YAML file and that Ravi can edit it using the Swagger editor. Ravi makes the required changes and commits the file to Git. He is excited to learn more about how the API reference is used by customers. 

## Read the backstory with an instructional video of how Ravi Iyer documented this API:

https://www.linkedin.com/pulse/rest-api-story-ravis-first-day-working-docs-after-moon-talwar/?trackingId=7K8JuWuzSQOsfghPQcXE%2BQ%3D%3D

## Watch the video:

[A Technical Writer's first REST API Assignment - How Ravi Desai worked with Swagger, YAML, and Git
](https://youtu.be/eHSX611dZ2Q?si=ToBrvz8DjZT6IUr0)


# Detailed Readme Of This API:

## Add Two Numbers API

To understand REST APIs and REST API Documentation, let's create a simple REST API, document it, and then use it using the REST API documentation we created. 


This is a simple REST API that performs addition of two numbers. It provides an endpoint `/add` to accept a POST request with JSON data containing `number1` and `number2` for addition.


### Requirements

- Python 3.x
- Flask (Install using `pip install flask`)


### Usage

1. Run the python program using the following command:

python AddTwoNumbers.py

**Tip**: You can also just download the program, open it in IDLE, and click **Run** > **Run Module** to get the REST API working. But, of course, you need to have python and flask installed on your computer.  

This will start the server on `http://loalhost:5000`  - you can also replace localhost with your computer IP, such as: `http://127.0.0.1:5000`, if you want to access the server from another computer on the same network.

2. Make a GET request to the `/add` endpoint using your preferred method (e.g., `curl`, Postman, etc.). The request should include the JSON data with `number1` and `number2` as keys and their respective values.

Example:

```bash
curl -G \
  --data-urlencode "number1=5" \
  --data-urlencode "number2=10" \
  http://127.0.0.1:5000/add
```

This command sends a GET request to `http://127.0.0.1:5000/add` with the query parameters `number1` and `number2`, set to `5` and `10`, respectively.

The response will be a JSON object with the result:

```
{
  "result": 15
}
```

#### If the JSON data is missing number1 or number2, or if they are not valid numbers, an error response will be returned:

```
{
  "error": "Invalid input. Please provide number1 and number2."
}
```

Contributions welcome - feel free to add what you wish.
