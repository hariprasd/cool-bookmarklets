from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

# Path for the JSON data file
DATA_FILE = 'bookmarklets.json'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    # Serve static files like style.css, script.js
    if filename in ['style.css', 'script.js']:
        return send_from_directory('.', filename)
    # For any other path, maybe return 404 or redirect to index
    return send_from_directory('.', 'index.html') # Or handle as 404

@app.route('/bookmarklets')
def get_bookmarklets():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Bookmarklets data file not found."}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding bookmarklets data."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use environment variable for port if available (e.g., for Heroku)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
