QR Code Generator

This project is a simple web application for generating QR codes. Users can provide a name and URL, and the application will generate a QR code that is automatically downloaded as an image file. The project is developed using Python Flask and the `qrcode` library.

Features:
- Enter a name and a URL to generate a custom QR code.
- Automatically downloads the QR code image.
- Minimalist design for ease of use.

Setup Instructions:
1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the dependencies listed in `requirements.txt`.
4. Run the application by executing `server.py`.
5. Open a browser and navigate to `http://localhost:5000`.

Project Structure:
- `templates/qr.html` : HTML file for the user interface.
- `server.py` : Main application file.
- `requirements.txt` : Python libraries required to run the application.

Dependencies:
- Flask: Lightweight WSGI web application framework.
- qrcode: Python library for generating QR codes.

Usage:
1. Launch the application in a browser.
2. Provide a file name and URL in the form.
3. Submit the form to download the QR code image.

License:
This project is open-sourced under the MIT License.

Contributions:
Contributions are welcome! Fork the repository and submit a pull request with improvements or new features.
