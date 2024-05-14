import zmq
import json

# Initialize a ZeroMQ context
context = zmq.Context() # Create a REP socket
socket = context.socket(zmq.REP)

# Bind the socket to a specific address
socket.bind("tcp://*:5555")

# Enter an infinite loop to continuously listen for messages
while True:
    # Receive a message from the client message = socket.recv_string()
    # Decode the message from JSON to a Python dictionary
    measurements = json.loads(message)
    
    # Open a new text file in write mode
    with open('recipe.txt', 'w') as f:
        # Iterate over the dictionary items
        for ingredient, measurement in measurements.items():
            # Write a line to the file in the format "ingredient: measurement"
            f.write(f"{ingredient}: {measurement}\n")

    # Open the file in read mode, read its contents into a string
    with open('recipe.txt', 'rb') as f: contents = f.read()
    # Send the bytes back to the client
    socket.send(contents)