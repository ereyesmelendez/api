from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def home():
    return "Home"

@app.route('/get-user, <user_is>')
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "johndoe@example.com"
    }

    extra = request.args.get('extra')
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200 # here we return the information back to the user in json. 200 is the stat code for success

@app.route('/add-user', methods=['POST'])
def add_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)