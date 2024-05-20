import zmq
import json

# Initialize a ZeroMQ context
context = zmq.Context()

# Create a REQ socket
socket = context.socket(zmq.REQ)

# Connect the socket to the server's address
socket.connect("tcp://localhost:5555")

# Define a dictionary of measurements
measurements = {
    "flour": "200g",
    "sugar": "100g",
    "butter": "50g"
}

# Send the measurements to the server
message = json.dumps(measurements)
print(measurements)
socket.send_string(message)

# Wait for the server's response (if any)
response = socket.recv_string()
print("Received response:", response)