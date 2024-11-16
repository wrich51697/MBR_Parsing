# MBR Parser Project

## Author
William Richmond

## Date
2024-11-16

## Class
CYBR-260-45

## Assignment
MBR Parsing

## Description
This project contains a Python program that parses the Master Boot Record (MBR) of a `.dd` disk image file (`block.dd`). The program extracts and processes the following information from the first partition entry:
- Status byte (Active/Inactive)
- Partition type (e.g., 0x83 for Linux)
- Starting address of the partition (LBA)

The project includes a server-client architecture, where the extracted partition entry is sent to a server for analysis.

## Project Structure

```text
MBR_Parsing/
├── docs/                   # Documentation folder
│   ├── mbr_structure.txt   # Detailed structure of the MBR
│   └── external_resources.txt  # Links to external downloads
├── logs/                   # Log files directory
│   ├── log.txt
│   ├── server_log.txt
│   └── run_log.txt
├── resources/              # Additional resources and disk image file
│   └── block.dd
├── tests/                  # Unit tests
│   └── test_mbr_parser.py
├── mbr_parser.py           # MBRParser class for parsing the MBR
├── partition_client.py     # Client script to send partition data to the server
├── server.py               # Server script to receive and process partition data
├── run.py                  # Main entry point for the program
├── README.md               # Project overview and usage instructions
├── requirements.txt        # List of dependencies
└── LICENSE                 # License information

```

## Requirements
- Python 3.8 or higher
- unittest (standard library)
- logging (standard library)

## Installation
1. Clone the repository or download the project files.
2. Ensure that block.dd is in the resources/ folder.
3. Install Python 3 if it’s not already installed.

## Usage
1. Run the entire program using the main entry point:
    ```bash
    python run.py
    ```
2. Start the server independently (if needed):
    ```bash
    python server.py
    ```
3. Run the unit tests:
    ```bash
    python -m unittest tests/test_mbr_parser.py
    ```

## Logging
Log files are automatically created in the logs/ directory:

- log.txt: Logs related to the MBR parsing (mbr_parser.py).
- server_log.txt: Logs related to server events (server.py).
- run_log.txt: Logs for the main entry point (run.py).
Check these files for detailed error information and program status.

## Resources
- [Wikipedia: Master Boot Record](https://en.wikipedia.org/wiki/Master_boot_record)

- `resources/mbr_structure.txt` - Detailed text file describing the MBR structure.

## Future Enhancements
- Add support for parsing additional partition entries (beyond the first).
- Include a more comprehensive analysis of different partition types.
- Implement multithreading for handling multiple client connections.
- Integrate a graphical user interface (GUI) for improved user experience.


### Summary of Changes:
1. **Updated Project Structure**: Reflects the new organization, including `logs/`, `resources/`, and `tests/` folders.
2. **Updated Usage Section**: Recommends using `run.py` as the primary entry point.
3. **Logging Section**: Clearly describes the purpose of each log file.
4. **Future Enhancements**: Added new ideas based on the current project capabilities.


