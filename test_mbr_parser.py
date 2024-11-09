# test_mbr_parser.py
# Author: William Richmond
# Date: 2024-11-09
# Class: CYBR-260-45
# Assignment: MBR Parsing Tests
# Description: Unit tests for the MBRParser class with enhanced error handling.

import unittest
from mbr_parser import MBRParser
import logging

# Configure logging for test output
logging.basicConfig(level=logging.DEBUG)

class TestMBRParser(unittest.TestCase):
    """Unit tests for the MBRParser class."""

    # function: setUpClass
    # purpose: Initialize the MBRParser with the 'block.dd' file
    # inputs: None
    # returns: None
    @classmethod
    def setUpClass(cls):
        try:
            cls.parser = MBRParser('block.dd')
            cls.parser.read_mbr()
        except Exception as e:
            logging.error(f"Setup error: {e}")
            raise

    # function: test_parse_partition_entry
    # purpose: Tests parsing of the first partition entry
    # inputs: None
    # returns: None
    def test_parse_partition_entry(self):
        try:
            status_byte, partition_type, first_sector_address = self.parser.parse_partition_entry()

            # Assertions to check the correctness of parsed values
            self.assertIsInstance(status_byte, int, "Status byte should be an integer.")
            self.assertIsInstance(partition_type, int, "Partition type should be an integer.")
            self.assertIsInstance(first_sector_address, int, "First sector address should be an integer.")

            # Print parsed values for verification
            print(f"Status Byte: {status_byte:#02x}")
            print(f"Partition Type: {partition_type:#02x}")
            print(f"First Sector Address: {first_sector_address}")

        except Exception as e:
            logging.error(f"Test error: {e}")
            self.fail(f"Test failed with error: {e}")

if __name__ == "__main__":
    unittest.main()
