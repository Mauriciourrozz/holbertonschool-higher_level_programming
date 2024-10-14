from flask import Flask, jsonify, request
app = Flask(__name__)

usuarios = {
    "pepe": {"name": "Pepe", "age": 28, "city": "Montevideo"},
    "fulano": {"name": "Fulano", "age": 30, "city": "Buenos aires"},
    "mengano": {"name": "Mengano", "age": 25, "city": "Salto"},
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def data():
    name_users = list(usuarios.keys())
    return name_users

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

@app.route("/add_user", methods=['GET', 'POST'])
def agregar_usuario():
    data = request.get_json()
    if 'username' not in data or not data['username']:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    usuarios[username] = {
    "name": data['name'],
    "age": data['age'],
    "city": data['city']
    }

if __name__ == "__main__":
    app.run()
