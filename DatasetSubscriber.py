import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

# Connect to the publisher's address
socket.connect("tcp://localhost:7786")  # Ensure this matches your publisher's address

# Subscribe to all messages (empty string means subscribe to all topics)
socket.setsockopt_string(zmq.SUBSCRIBE, "")

try:
    # Receive and process messages
    for _ in range(10):  # Adjust to receive the same number of records as published
        message = socket.recv()
        print(f"Received: {message.decode('utf-8')}")  # Decode the message if needed
except zmq.ZMQError as e:
    print(f"ZMQError: {e}")
except KeyboardInterrupt:
    pass

# Close the socket and context
socket.close()
context.term()

print("Subscriber finished receiving messages.")