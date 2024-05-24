import zmq
import json

# Create a ZeroMQ context
context = zmq.Context()

# Create a REQ (request) socket
socket = context.socket(zmq.REQ)

# Connect the socket to the server's address
socket.connect("tcp://localhost:5555")

# Create a list of dictionaries
measurements = [
    {"Butter": 225},
    {"Strong Flour": 145},
    {"Strong Flour": 55}
]

# Convert the list of dictionaries to a JSON string
request = json.dumps(measurements)

# Send the request to the server
socket.send_string(request)

# Wait for the server's response
response = socket.recv_string()

# Write the response to a file
with open('ingredients.txt', 'w') as f:
    f.write(response)