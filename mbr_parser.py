# mbr_parser.py
# Author: William Richmond
# Date: 2024-11-16
# Class: CYBR-260-45
# Assignment: MBR Parsing
# Description: Contains the MBRParser class to parse the Master Boot Record (MBR) from a .dd file.
# Revised on: 2024-11-16

import logging
import os

# Configure logging
logging.basicConfig(
    filename='logs/log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MBRParser:
    # Class to parse the Master Boot Record (MBR) from a .dd file.

    # function: __init__
    # purpose: Initialize the MBRParser with the filename of the .dd file
    # inputs: filename (str)
    # returns: None
    def __init__(self, filename):
        if not os.path.isfile(filename):
            logging.error(f"Invalid file path: {filename}")
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        self.filename = filename
        self.mbr = None
        logging.info(f"MBRParser initialized with file: {filename}")

    # function: read_mbr
    # purpose: Reads the first 512 bytes of the .dd file (the MBR)
    # inputs: None
    # returns: None
    def read_mbr(self):
        try:
            with open(self.filename, 'rb') as file:
                self.mbr = file.read(512)
                if len(self.mbr) != 512:
                    logging.error("Failed to read the full MBR (512 bytes expected).")
                    raise ValueError("MBR data is incomplete.")
            logging.info("MBR read successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.filename}")
            raise
        except PermissionError:
            logging.error(f"Permission denied when accessing: {self.filename}")
            raise
        except OSError as e:
            logging.error(f"OS error while reading the file: {e}")
            raise
        except Exception as e:
            logging.exception(f"Unexpected error while reading MBR: {e}")
            raise

    # function: extract_first_partition
    # purpose: Extracts the first partition entry from the MBR
    # inputs: None
    # returns: partition_entry (bytes)
    def extract_first_partition(self):
        try:
            if not self.mbr:
                logging.error("MBR data not loaded. Call read_mbr() first.")
                raise ValueError("MBR data not loaded. Call read_mbr() first.")
            partition_entry = self.mbr[0x1BE:0x1CE]
            logging.info("First partition entry extracted successfully.")
            return partition_entry
        except IndexError:
            logging.error("Error extracting partition entry: Data index out of range.")
            raise
        except Exception as e:
            logging.exception(f"Unexpected error while extracting partition entry: {e}")
            raise