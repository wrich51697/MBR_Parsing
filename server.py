# server.py
# Author: William Richmond
# Date: 2024-11-16
# Class: CYBR-260-45
# Assignment: MBR Partition Extraction Server
# Description: Receives partition entry and displays its details.
# Revised on:

import socket
import struct
import logging

# Configure logging
logging.basicConfig(
    filename='logs/server_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# function: parse_partition_entry
# purpose: Parses the partition entry and prints status, partition type, and starting address
# inputs: partition_entry (bytes)
# returns: None
def parse_partition_entry(partition_entry):
    try:
        # Validate input length
        if len(partition_entry) != 16:
            logging.error("Partition entry length is invalid. Expected 16 bytes.")
            return

        # Extract values from the partition entry
        status = partition_entry[0]
        partition_type = partition_entry[4]
        start_address = struct.unpack('<I', partition_entry[8:12])[0]

        # Print parsed values
        logging.info(f"Drive Status: {'Active' if status == 0x80 else 'Inactive'}")
        logging.info(f"Partition Type: {hex(partition_type)}")
        logging.info(f"Starting Address (LBA): {start_address}")

        print(f"Drive Status: {'Active' if status == 0x80 else 'Inactive'}")
        print(f"Partition Type: {hex(partition_type)}")
        print(f"Starting Address (LBA): {start_address}")

    except struct.error as e:
        logging.error(f"Data unpacking error: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error while parsing partition entry: {e}")

# function: start_server
# purpose: Starts the server to listen for incoming partition data
# inputs: host (str), port (int)
# returns: None
def start_server(host='127.0.0.1', port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Set a timeout to prevent hanging connections
            server_socket.settimeout(10.0)
            server_socket.bind((host, port))
            server_socket.listen()
            logging.info(f"Server listening on {host}:{port}...")
            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                logging.info(f"Connection established with {addr}")
                print(f"Connection established with {addr}")

                # Receive data with error handling
                try:
                    partition_entry = conn.recv(16)
                    if len(partition_entry) == 16:
                        parse_partition_entry(partition_entry)
                    else:
                        logging.error("Received data length mismatch. Expected 16 bytes.")
                        print("Received data length mismatch.")
                except socket.timeout:
                    logging.error("Socket timeout while receiving data.")
                    print("Socket timeout while receiving data.")
                except Exception as e:
                    logging.exception(f"Error receiving data: {e}")

    except socket.error as e:
        logging.error(f"Socket error: {e}")
        print(f"Socket error: {e}")
    except Exception as e:
        logging.exception(f"Unexpected server error: {e}")
        print(f"Unexpected server error: {e}")

# Main execution block
if __name__ == "__main__":
    start_server()