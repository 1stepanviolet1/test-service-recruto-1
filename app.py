from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main_handler():
    _name = request.args.get('name', None)
    _msg = request.args.get('message', None)

    if _name is None or _msg is None:
        return jsonify({
            'error': "bad request",
            'message': "arguments not found"
        }), 400

    return f"Hello {_name}! {_msg}!", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


