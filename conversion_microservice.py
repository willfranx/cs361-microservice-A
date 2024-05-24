import zmq
import json

# Create a ZeroMQ context
context = zmq.Context()

# Create a REP (reply) socket
socket = context.socket(zmq.REP)

# Bind the socket to a TCP address
socket.bind("tcp://localhost:5555")

while True:
    # Wait for a request from the client
    request = socket.recv_string()

    # Convert the request to a list of dictionaries
    measurements = json.loads(request)

    # Create an empty list to hold the ingredient strings
    ingredient_strings = []

    for measurement in measurements:
        for ingredient, amount in measurement.items():
            # Add the ingredient string to the list
            ingredient_strings.append(f'{ingredient}: {amount}')

    # Join the ingredient strings into a single string
    response = '\n'.join(ingredient_strings)

    # Send the response
    socket.send_string(response)