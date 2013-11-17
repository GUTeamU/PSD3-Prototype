# Requirements

* Python 2.7

# Installation

1. Clone the repository

2. Initialise the database:
```python
from HelperFunctions import init_db
init_db(True)
```

# Usage

## Exporting couse and student data

Run the export script and follow the instructions:
```bash
python export.py
```

The files will be saved in the current working directory.

## Importing student attendance information

Run the import script and follow the instructioons:
```bash
python import.py
```

If given a relative path the script will look for the barcode
data file in the current working directory.
