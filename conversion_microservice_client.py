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

# Convert the response back to a dictionary
response_dict = json.loads(response)

# Write the dictionary to a .txt file
with open('response.txt', 'w') as f:
    for key, value in response_dict.items():
        f.write(f'{key}: {value}\n')