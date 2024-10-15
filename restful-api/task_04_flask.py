from flask import Flask, jsonify, request
app = Flask(__name__)

usuarios = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    name_users = list(usuarios.keys())
    return jsonify(name_users)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>", methods=['GET'])
def devolver_segun_username(username):
    usuario = usuarios.get(username)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    nombre = data["name"]
    edad = data["age"]
    ciudad = data["city"]

    if not username:
        return jsonify({"error":"Username is required"}), 400

    usuarios[username] = {
        'username': username,
        'name': nombre,
        'age': edad,
        'city': ciudad
    }
    
    return jsonify({"message": "User added", "user": usuarios[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
