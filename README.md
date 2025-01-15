# SearchPatterns

### Description

SearchPatterns is a Python script designed to search for specific patterns in files. It allows users to efficiently locate and extract data matching given patterns within a directory of files. This is particularly useful for tasks like log analysis, data extraction, and code review.

### Features

- **Pattern Matching:** Uses regular expressions to find patterns in files.

- **File Traversal:** Scans through all files in the specified directory.

- **Customizable:** Users can specify the pattern and the directory to search.

### Requirements

The script requires Python 3.6 or higher. Ensure that all dependencies listed in **requirements.txt** are installed.

### Installation

- Clone the repository or download the ZIP file.

```bash
git clone https://github.com/your-repository/SearchPatterns.git
```

- Navigate to the project directory:

```bash
cd SearchPatterns
```

- Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the script with the following command:

```bash
python searchPatterns.py --pattern "<REGEX_PATTERN>" --directory "<DIRECTORY_PATH>"
```

### Arguments

- --**pattern**: The regular expression pattern to search for.

- --**directory**: The path to the directory where files will be scanned.

### Example

Search for email addresses in the logs directory:

```bash
python searchPatterns.py --pattern "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" --directory "./logs"
```

### File Structure

```bash
SearchPatterns/
|├── README.md          # Documentation
|├── requirements.txt    # Dependencies
|└── searchPatterns.py  # Main script
```



### Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.



### Support

If you encounter any issues or have questions, please contact s.p@castsoftware.com

