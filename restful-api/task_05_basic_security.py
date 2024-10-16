from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token


app = Flask(__name__)
auth = HTTPBasicAuth()

usuarios = {
    "pepe": {"username": "pepe", "password": generate_password_hash("pepito"), "role": "user"},
    "tito": {"username": "tito", "password": generate_password_hash("titito"), "role": "admin"}
  }

@auth.verify_password
def verify_password(nombreUsuario, password):
    if nombreUsuario in usuarios and check_password_hash(usuarios[nombreUsuario]['password'], password):
        return nombreUsuario

@app.route('/')
def home():
    return "Hello!"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

app.config['JWT_SECRET_KEY'] = 'Holamundo'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if not usuarios or not check_password_hash(usuarios[username]['password'], password):
        return {"error": "access denied"}, 401
    token = create_access_token(identity={'username': username, 'role': usuarios[username]['role']})
    return {"access_token": token}, 200

if __name__ == '__main__':
    app.run()
