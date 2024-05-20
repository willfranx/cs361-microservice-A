import zmq
import json

# Initialize a ZeroMQ context
context = zmq.Context()

# Create a REP socket
socket = context.socket(zmq.REP)

# Bind the socket to an address
socket.bind("tcp://localhost:5555")

# Define a conversion factor from grams to ounces
grams_to_ounces = 0.035274

while True:
    # Wait for a message from the client
    message = socket.recv_string()
    measurements = json.loads(message)

    # Convert the measurements from grams to ounces
    converted_measurements = {ingredient: str(float(amount[:-1]) * grams_to_ounces) + 'oz'
                              for ingredient, amount in measurements.items()}

    # Send the converted measurements back to the client
    response = json.dumps(converted_measurements)
    socket.send_string(response)