import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)

# Connect to the publisher's address
socket.connect("tcp://localhost:7786")  # Ensure this matches your publisher's address

# Subscribe to all messages (empty string means subscribe to all topics)
socket.setsockopt_string(zmq.SUBSCRIBE, "")

# Specify the duration to run the subscriber in seconds
duration_seconds = 10  # Example: Run for 30 seconds

start_time = time.time()

while (time.time() - start_time) < duration_seconds:
    try:
        # Receive message
        message = socket.recv_string()
        print(f"Received: {message}")
    except zmq.ZMQError as e:
        print(f"ZMQError: {e}")
        break
    except KeyboardInterrupt:
        break

# Close the socket and context after the duration ends
socket.close()
context.term()

print("Subscriber finished.")