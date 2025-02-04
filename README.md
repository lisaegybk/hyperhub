# HyperHub

HyperHub is a Python-based utility designed to centralize and simplify the application of software patches on Windows systems. It aims to maintain system integrity by ensuring that all necessary patches are applied efficiently and without user intervention.

## Features
- Automatically discovers available `.msu` patch files in the specified directory.
- Applies patches using the Windows Update Standalone Installer (`wusa.exe`).
- Logs all operations, including successful applications and errors, to a log file for review.

## Requirements
- Python 3.x
- Windows operating system
- Administrative privileges to apply patches

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HyperHub.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd HyperHub
   ```

## Usage
1. Place the patch files (`.msu`) in the `patches` directory.
2. Run the script with administrative privileges:
   ```bash
   python hyperhub.py
   ```
3. Check the `hyperhub.log` file for logs regarding the patch application process.

## Logging
HyperHub creates a log file named `hyperhub.log` in the same directory. This log file records all actions taken by the application, including successful patch applications and any errors encountered.

## Notes
- Ensure that the patch files are compatible with your system before applying them.
- The application runs silently and will not restart the system automatically after patches are applied. It is recommended to reboot the system manually after applying patches.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## Contact
For any questions or suggestions, please open an issue on the [GitHub repository](https://github.com/yourusername/HyperHub/issues).