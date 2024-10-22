
# Driver Track System

This project is a **Driver Track System** designed to manage and evaluate drivers' interactions during their trips. The system processes trip data, evaluates driver performance, and generates detailed reports based on predefined criteria.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Driver Track System is a Python-based application that processes and validates trip data for drivers. It generates reports on driver performance, focusing on interactions with students during the trips, and provides evaluations based on different criteria like time spans and presence checks. The system supports multiple languages including Arabic, Kurdish Sorani, and English.

## Features
- **Data Loading**: Load and preprocess trip and driver data from Excel files.
- **Driver Management**: Manage driver information such as vehicle type, usage evaluation, and notes for performance.
- **Trip Validation**: Validate trip data for interactions, time ranges, and other specific conditions.
- **Report Generation**: Generate reports based on driver performance and save them using a template Excel file.
- **Multi-language Support**: Supports translations for various messages and notes in Arabic, Kurdish Sorani, and English.

## Project Structure
```
my_project/
│
├── data/                   # Folder for input files (e.g., templates and driver info)
│   ├── template.xlsx       # Excel template used for report generation
│   └── drivers_info.xlsx   # Sample driver information file
├── my_project/             # Main package folder containing the code
│   ├── constants.py
│   ├── data_loader.py
│   ├── driver.py
│   ├── report_generator.py
│   ├── translations.py
│   ├── trip.py
│   │── utils.py
│   ├── main.py                 # Main script to run the project
├── README.md               # Documentation file
├── .gitignore              # File for excluding unnecessary files from version control
└── driver track.bat        # Batch file for automating the run process
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/my_project.git
   cd my_project
   ```

2. **Install Dependencies**

## Usage

1. Place your input files `export.xlsx` for trip data in the `Downloads` directory, `drivers_info.xlsx` for driver info in the `data` directory.
2. Run the application
3. The application will process the data and generate a report (`driver_track.xlsx`) in your Downloads folder.

Alternatively, you can run the batch file provided (`driver track.bat`) for automation.

## Dependencies
The project depends on the following libraries:
- `pandas` For data manipulation and loading Excel files.
- `openpyxl` For working with Excel files, especially for reading and writing reports.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
