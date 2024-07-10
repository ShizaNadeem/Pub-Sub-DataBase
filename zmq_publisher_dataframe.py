import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:7786")  # Binding to TCP socket on port 7786

# Specify the duration to run the publisher in seconds
duration_seconds = 10  # Example: Run for 30 seconds

start_time = time.time()

while (time.time() - start_time) < duration_seconds:
    # Generate a random number
    random_number = random.randint(1, 100)

    # Convert the number to bytes (assuming Python 3)
    message = str(random_number).encode('utf-8')

    # Publish the message
    socket.send(message)
    print(f"Published: {random_number}")

    # Sleep for a while before publishing the next number
    time.sleep(1)

# Close the socket and context after the duration ends
socket.close()
context.term()

print("Publisher finished.")
