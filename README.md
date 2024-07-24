# RSS Feed Validator and Downloader

This Flask application allows users to verify RSS feed URLs and download the feed data as a JSON file.

## Features

- **RSS Feed Validation**: Checks if the provided URL is a valid RSS feed.
- **Feed Parsing**: Extracts feed details including entries, images, and descriptions.
- **JSON Download**: Saves the feed data to a JSON file and provides a download link.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/rss-feed-validator.git
    cd rss-feed-validator
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/`.

3. **Submit an RSS feed URL** through the form on the homepage.

4. **View the result**: If the URL is valid, the feed information will be displayed, and you can download the JSON file by clicking the provided link. If the URL is invalid, an error message will be shown.

## Project Structure
rss-feed-validator/
│
├── main.py # Main Flask application script
├── requirements.txt # List of dependencies
├── templates/
│ ├── index.html # HTML template for the input form and error messages
│ └── result.html # HTML template for displaying feed information and download link
└── README.md # This file


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
If you have suggestions or improvements, please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Dependencies

- Flask
- requests
- feedparser

To install these dependencies, use the `requirements.txt` file:

```plaintext
Flask==2.2.3
requests==2.28.1
feedparser==6.0.10


