# test_mbr_parser.py
# Author: William Richmond
# Date: 2024-11-09
# Class: CYBR-260-45
# Assignment: MBR Parsing Tests
# Description: Unit tests for the MBRParser class with enhanced error handling.
# Revised on: 2024-11-16


import unittest
from mbr_parser import MBRParser
import logging
import struct

# Configure logging for test output
logging.basicConfig(level=logging.DEBUG)

class TestMBRParser(unittest.TestCase):
    # Unit tests for the MBRParser class.

    # function: setUpClass
    # purpose: Initialize the MBRParser with the 'block.dd' file
    # inputs: None
    # returns: None
    @classmethod
    def setUpClass(cls):
        try:
            cls.parser = MBRParser('resources/block.dd')
            cls.parser.read_mbr()
        except Exception as e:
            logging.error(f"Setup error: {e}")
            raise

    # function: test_extract_first_partition
    # purpose: Tests the extraction of the first partition entry
    # inputs: None
    # returns: None
    def test_extract_first_partition(self):
        try:
            # Extract the first partition entry (16 bytes)
            partition_entry = self.parser.extract_first_partition()

            # Ensure the extracted entry is of correct length
            self.assertEqual(len(partition_entry), 16, "Partition entry should be 16 bytes long.")

            # Parse the partition entry for testing
            status_byte = partition_entry[0]
            partition_type = partition_entry[4]
            start_address = struct.unpack('<I', partition_entry[8:12])[0]

            # Assertions to check the correctness of parsed values
            self.assertIsInstance(status_byte, int, "Status byte should be an integer.")
            self.assertIsInstance(partition_type, int, "Partition type should be an integer.")
            self.assertIsInstance(start_address, int, "Starting address should be an integer.")

            # Print parsed values for verification
            print(f"Status Byte: {status_byte:#02x}")
            print(f"Partition Type: {partition_type:#02x}")
            print(f"Starting Address (LBA): {start_address}")

        except Exception as e:
            logging.error(f"Test error: {e}")
            self.fail(f"Test failed with error: {e}")

if __name__ == "__main__":
    unittest.main()