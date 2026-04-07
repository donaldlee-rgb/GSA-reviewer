# Contract Redline Analyzer

## Description
The Contract Redline Analyzer is a powerful tool designed to help users effectively analyze and manage contract redlines. It identifies changes between contract versions, making it easier to understand modifications, track changes, and ensure compliance.

## Installation
To install the Contract Redline Analyzer, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/donaldlee-rgb/GSA-reviewer.git
   cd GSA-reviewer
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Ensure you have Python and any required libraries if applicable. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start
Once the installation is complete, you can start using the analyzer with the following command:
```bash
python analyzer.py <contract_version_1> <contract_version_2>
```

## Usage Examples
Here are some examples of how to use the Contract Redline Analyzer:

### Example 1: Basic Comparison
To analyze two contract versions:
```bash
python analyzer.py contract_v1.docx contract_v2.docx
```

### Example 2: Outputting Results to a File
You can save the output to a file using:
```bash
python analyzer.py contract_v1.docx contract_v2.docx --output results.txt
```

## API Reference
### `analyze_contract(version_one: str, version_two: str) -> dict`
Analyzes two versions of a contract and returns a dictionary with the changes.

#### Parameters
- `version_one`: Path to the first contract version.
- `version_two`: Path to the second contract version.

#### Returns
A dictionary containing changes between the two versions.

## Troubleshooting Guide
- **Problem:** The script fails to run.
  - **Solution:** Ensure all dependencies are installed correctly and Python is added to your PATH.

- **Problem:** The output is not as expected.
  - **Solution:** Double-check the paths of the contract versions and ensure they are properly formatted.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
