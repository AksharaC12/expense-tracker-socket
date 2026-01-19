import json

def decode_request(data):
    try:
        return json.loads(data.decode())
    except Exception:
        return None

def encode_response(status, message, data=None):
    response = {
        "status": status,
        "message": message
    }
    if data is not None:
        response["data"] = data

    return json.dumps(response).encode()
