# ZeroMQ Publisher-Subscriber Example

## Overview

This project demonstrates how to implement a publisher-subscriber pattern using ZeroMQ for message passing. ZeroMQ is a lightweight messaging library that allows you to design distributed applications easily.

## Components
### 1. Publisher (`publisher.py`)
The publisher script (`publisher.py`) does the following:

- Generates or retrieves data (e.g., from a CSV file or generates random numbers).
- Serializes the data (e.g., to JSON format).
- Publishes the serialized data to a specified address using ZeroMQ PUB socket.

### 2. Subscriber (`subscriber.py`)
The subscriber script (`subscriber.py`) does the following:

- Connects to the publisher's address using ZeroMQ SUB socket.
- Subscribes to receive messages (in this case, all topics).
- Receives and processes messages from the publisher.
- Prints or processes the received messages.

## Dependencies
- Python 3.x
- PyZMQ (Python bindings for ZeroMQ)
- pandas (for handling data, if applicable)

## Usage
1. **Setup Environment:**
   - Install Python 3.x and necessary packages (`pyzmq`, `pandas`).

2. **Run Publisher:**
   - Execute `publisher.py` to start publishing messages.
   - Adjust the script to publish data from a CSV file or generate random data as needed.

3. **Run Subscriber:**
   - Execute `subscriber.py` to start receiving and processing messages from the publisher.
   - Adjust the script to handle the received data according to your application's needs.

4. **Adjust Configuration:**
   - Modify the publisher and subscriber scripts to match your specific use case (e.g., change message formats, adjust socket bindings).

## Example Scenario
- The provided examples include:
  - Publishing data from a CSV file (`online_retail_sales_dataset.csv`) using JSON serialization.
  - Publishing random numbers for a specified duration.
  - Subscribing to these messages and printing them.

## Notes
- Ensure both scripts (`publisher.py` and `subscriber.py`) are running and connected to the same network address and port.
- Handle exceptions and errors appropriately based on your deployment environment.
