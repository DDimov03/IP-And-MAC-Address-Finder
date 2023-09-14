# IP and MAC Address Finder

A simple Python application to retrieve IP and MAC addresses for a given domain name. This application utilizes the `getmac` library to fetch MAC addresses and the `socket` library to obtain IP addresses.

## Features

- Input a domain name and fetch its IP and MAC addresses.
- Save the results to a text file.
- User-friendly interface with a themed style for better aesthetics.
- Watermark label with the author's name.

## Prerequisites

Before running the application, make sure you have the required Python libraries installed:

```bash
pip install getmac tkinter ttkthemes
Usage
Launch the application by running main.py.
Enter a domain name or type 'suggestion' for help (e.g., google).
Click the "Fetch Addresses" button to retrieve IP and MAC addresses.
View the results in the text box.
Click the "Save to File" button to save the results to addresses.txt.
Screenshots
Screenshot

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Denis Dimov
Acknowledgments
Special thanks to the developers of getmac and ttkthemes libraries.
