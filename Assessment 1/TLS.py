TLS Implentation:
********************
from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Wisecow Application!"})

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"received": data, "message": "Data processed successfully!"})

if __name__ == "__main__":
    # Run the Flask application over HTTPS (TLS)
    app.run(
        host='0.0.0.0', 
        port=5000, 
        ssl_context=('certs/server.crt', 'certs/server.key')  # Using your self-signed certificates
    )
