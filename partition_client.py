# partition_client.py
# Author: William Richmond
# Date: 2024-11-16
# Class: CYBR-260-45
# Assignment: MBR Partition Client
# Description: Sends extracted partition entry to the server.
# Revised on:

import socket
import logging
from mbr_parser import MBRParser

# Configure logging
logging.basicConfig(
    filename='logs/log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PartitionClient:
    # Class to handle networking for sending partition data to a server.

    # function: __init__
    # purpose: Initialize the PartitionClient with server host and port
    # inputs: host (str), port (int)
    # returns: None
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port

    # function: send_partition_data
    # purpose: Sends the extracted partition data to the server
    # inputs: partition_data (bytes)
    # returns: None
    def send_partition_data(self, partition_data):
        try:
            # Validate that partition_data is exactly 16 bytes
            if len(partition_data) != 16:
                logging.error("Invalid partition data length. Expected 16 bytes.")
                raise ValueError("Partition data must be 16 bytes long.")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                # Set a timeout to prevent hanging connections
                client_socket.settimeout(10.0)
                client_socket.connect((self.host, self.port))
                client_socket.sendall(partition_data)
                logging.info("Partition data sent to server successfully.")
                print("Partition data sent to server successfully.")

        except ConnectionRefusedError:
            logging.error("Connection refused by the server. Ensure the server is running.")
            print("Connection refused by the server. Ensure the server is running.")
        except TimeoutError:
            logging.error("Socket timeout. The server did not respond.")
            print("Socket timeout. The server did not respond.")
        except ValueError as e:
            logging.error(f"Data validation error: {e}")
            print(f"Data validation error: {e}")
        except Exception as e:
            logging.exception(f"Unexpected error while sending data to server: {e}")
            print(f"Unexpected error while sending data to server: {e}")

# Main execution block
if __name__ == "__main__":
    parser = MBRParser('resources/block.dd')
    parser.read_mbr()
    partition_data = parser.extract_first_partition()

    client = PartitionClient()
    client.send_partition_data(partition_data)
