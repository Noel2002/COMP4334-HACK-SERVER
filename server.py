from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Set up a file handler specifically for logging URLs
file_handler = logging.FileHandler('log.txt')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Create a separate logger for URL logging
url_logger = logging.getLogger('urlLogger')
url_logger.setLevel(logging.INFO)
url_logger.addHandler(file_handler)

@app.route('/report', methods=['POST'])
def report():
    # Check if the request contains JSON data
    if request.is_json:
        data = request.get_json()
        url = data.get('url')
        
        if url:
            # Log the URL with a timestamp to the file
            url_logger.info(url)
            return jsonify({"message": "URL logged successfully"}), 200
        else:
            return jsonify({"error": "URL field is missing"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    # Run the server on port 8080
    app.run(debug=True, port=8080)