import pandas as pd
import zmq
import json  # Import the json module for serialization
import time

# Load dataset into pandas DataFrame
df = pd.read_csv('online_retail_sales_dataset.csv')

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:7786")  # Binding to TCP socket on port 7786

# Iterate through the first 10 rows of the DataFrame
for index, row in df.head(10).iterrows():
    # Convert row to a dictionary for easy serialization
    data_dict = row.to_dict()

    # Convert the dictionary to a JSON string (you can use any serialization method)
    message = json.dumps(data_dict).encode('utf-8')

    # Publish the message
    socket.send(message)
    print(f"Published: {data_dict}")

    # Optionally, add a small delay between each transmission
    time.sleep(0.1)  # Adjust as needed

# Close the socket and context after all rows are transmitted
socket.close()
context.term()

print("Data transmission completed for 10 records.")