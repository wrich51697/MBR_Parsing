# run.py
# Author: William Richmond
# Date: 2024-11-16
# Class: CYBR-260-45
# Assignment: MBR Parsing Program Entry Point
# Description: Single entry point to start the server, parse the MBR, and send data to the server.
# Revised on:

import threading
import time
import logging
from mbr_parser import MBRParser
from partition_client import PartitionClient
from server import start_server

# Configure logging
logging.basicConfig(
    filename='logs/run_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# function: start_server_thread
# purpose: Starts the server in a separate thread
# inputs: None
# returns: None
def start_server_thread():
    try:
        # Runs the server in a separate thread
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        logging.info("Server started in a separate thread.")
        print("Server started in a separate thread.")
    except Exception as e:
        logging.exception(f"Error starting server thread: {e}")
        print(f"Error starting server thread: {e}")

# function: main
# purpose: Main function to orchestrate the flow of the program
# inputs: None
# returns: None
def main():
    try:
        # Start the server
        start_server_thread()

        # Give the server a moment to start up
        time.sleep(1)

        # Initialize MBRParser and read the MBR data
        parser = MBRParser('resources/block.dd')
        parser.read_mbr()
        partition_data = parser.extract_first_partition()
        logging.info("Partition entry extracted successfully.")
        print("Partition entry extracted:", partition_data)

        # Initialize PartitionClient and send the data to the server
        client = PartitionClient()
        client.send_partition_data(partition_data)
        logging.info("Partition data sent to the server successfully.")
        print("Partition data sent to the server.")

    except Exception as e:
        logging.exception(f"Unexpected error in main execution: {e}")
        print(f"Unexpected error: {e}")

# Main execution block
if __name__ == "__main__":
    main()