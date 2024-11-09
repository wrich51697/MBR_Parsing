# mbr_parser.py
# Author: William Richmond
# Date: 2024-11-09
# Class: CYBR-260-45
# Assignment: MBR Parsing
# Description: Contains the MBRParser class to parse the Master Boot Record (MBR) from a .dd file,
# with added logging and enhanced error handling.

import logging
import os

# Configure logging
logging.basicConfig(
    filename='log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MBRParser:
    """Class to parse the Master Boot Record (MBR) from a .dd file."""

    # function: __init__
    # purpose: Initialize the MBRParser with the filename of the .dd file
    # inputs: filename (str)
    # returns: None
    def __init__(self, filename):
        self.filename = filename
        self.mbr = None

        # Check if the file exists
        if not os.path.isfile(self.filename):
            logging.error(f"File not found: {self.filename}")
            raise FileNotFoundError(f"The file '{self.filename}' does not exist.")

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
            logging.critical(f"File not found: {self.filename}")
            raise
        except PermissionError:
            logging.critical(f"Permission denied when accessing: {self.filename}")
            raise
        except Exception as e:
            logging.exception(f"Unexpected error while reading MBR: {e}")
            raise

    # function: parse_partition_entry
    # purpose: Parses the first partition entry located at offset 0x1BE
    # inputs: None
    # returns: tuple (status_byte, partition_type, first_sector_address)
    def parse_partition_entry(self):
        try:
            if not self.mbr:
                logging.error("MBR data not loaded. Call read_mbr() first.")
                raise ValueError("MBR data not loaded. Call read_mbr() first.")

            partition_entry_offset = 0x1BE

            # Extract status byte (1 byte)
            status_byte = self.mbr[partition_entry_offset]

            # Extract partition type (1 byte at 1BE + 4)
            partition_type = self.mbr[partition_entry_offset + 4]

            # Extract the address of the first sector (4 bytes at 1BE + 8)
            first_sector_address = int.from_bytes(self.mbr[partition_entry_offset + 8:partition_entry_offset + 12], 'little')

            logging.info("Partition entry parsed successfully.")
            return status_byte, partition_type, first_sector_address

        except IndexError:
            logging.error("Error parsing partition entry: Data index out of range.")
            raise
        except Exception as e:
            logging.exception(f"Unexpected error while parsing partition entry: {e}")
            raise

