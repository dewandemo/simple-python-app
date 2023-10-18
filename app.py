from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint to echo a hello message with variable input
@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return f'Hello, {name}!'

# Endpoint to show app health
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)
