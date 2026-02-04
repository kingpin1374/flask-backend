from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/process', methods=['POST'])
def process_data():
    # Be robust if client sends invalid JSON or no body
    data = request.get_json(silent=True) or {}
    name = data.get('name')
    email = data.get('email')

    if name and email:
        # No DB operation here; just acknowledge receipt
        response_message = f"Success! Backend received: {name} ({email})"
        status_code = 200
        response_body = {
            "status": "success",
            "message": response_message,
            "received_data": {"name": name, "email": email}
        }
    else:
        response_message = "Backend received incomplete data."
        status_code = 400
        response_body = {"status": "error", "message": response_message}

    return jsonify(response_body), status_code

@app.route('/api/process', methods=['POST'])
def api_process_data():
    # Be robust if client sends invalid JSON or no body
    data = request.get_json(silent=True) or {}
    name = data.get('name')
    email = data.get('email')

    if name and email:
        response_message = f"Success! Backend received: {name} ({email})"
        status_code = 200
        response_body = {
            'status': 'success',
            'message': response_message,
            'received_data': {'name': name, 'email': email}
        }
    else:
        response_message = "Backend received incomplete data."
        status_code = 400
        response_body = {'status': 'error', 'message': response_message}

    return jsonify(response_body), status_code
    
if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=8000)