# MBR Parser Project

## Author
William Richmond

## Date
2024-11-09

## Class
CYBR-260-45

## Assignment
MBR Parsing

## Description
This project contains a Python program that parses the Master Boot Record (MBR) of a `.dd` disk image file (named `block.dd`). The program extracts the following information from the MBR:
- Status byte of the first partition entry
- Partition type
- Address of the first sector of the first partition

## Project Structure 

```text
mbr_parser_project/
├── mbr_parser.py         # MBRParser class
├── test_mbr_parser.py    # Unit tests
├── block.dd              # The disk image file
├── log.txt               # Log file (auto-generated)
├── README.md             # Project documentation
├── resources/            # Additional resources and references
│   └── mbr_structure.txt # Diagram of the MBR structure (optional)
└── __init__.py           # Makes the folder a package (optional)
```


## Requirements
- Python 3.8 or higher
- `unittest` (standard library)
- `logging` (standard library)

## Installation
1. Clone the repository or download the project files.
2. Ensure that `block.dd` is in the same directory as the Python files.
3. Install Python 3 if not already installed.

## Usage
1. Run the MBR parsing script:
   ```bash
   python mbr_parser.py
   ```
    
2. Run the unit tests:
   ```Bash
    python -m unittest test_mbr_parser.py
    ```
## Logging
All logs are saved to log.txt. Check this file for detailed error information and program status.

## Resources

- [Wikipedia: Master Boot Record](https://en.wikipedia.org/wiki/Master_boot_record)
- `resources/mbr_structure.png` - Diagram of the MBR structure for reference.


## Future Enhancements
- Add support for parsing additional partition entries.
- Include more detailed analysis of the partition types.
- Integrate with a GUI for easier use.