# QR Code Generator

This project is a simple web application that generates QR codes. Users provide a name and a URL, and the application generates a QR code that is immediately downloaded as an image file. Built using Python Flask and the `qrcode` library, this tool is straightforward and efficient.

## Features
- Generate QR codes by entering a name and a URL.
- Automatically download the QR code image upon submission.
- Minimalist design for ease of use.

## Getting Started

### Requirements
To run this project, ensure you have the following installed:
- Python 3.7 or later
- pip (Python package installer)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/SuryaBramananthan24/QR-Code-Generator.git
   cd QR-Code-Generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python server.py
   ```

5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Open the application in your browser.
2. Fill out the form with the desired file name and the URL to encode.
3. Submit the form to generate and download the QR code image.

## Folder Structure
```
QR-Code-Generator/
|-- templates/
|   |-- qr.html        # HTML file for the UI
|-- server.py          # Main Flask application file
|-- requirements.txt   # List of dependencies
|-- README.md          # Documentation
```

## Dependencies
This project uses the following Python libraries:
- Flask: Web framework
- qrcode: Library for generating QR codes

Install them with:
```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements or new features.

