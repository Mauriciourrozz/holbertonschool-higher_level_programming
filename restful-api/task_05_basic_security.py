from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


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
    return "Basic Auth: Access Granted", 200

app.config['JWT_SECRET_KEY'] = 'super secret password'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get['username']
    password = data.get['password']

    if not usuarios or not check_password_hash(usuarios['password'], password):
        return {"error": "access denied"}, 401

    token = create_access_token(identity={'username': username, 'role': usuarios[username]['role']})
    return {"access_token": token}, 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.route("/admin-only")
@jwt_required()
def admin_only():
    traer_rol_usuario = get_jwt_identity()
    if traer_rol_usuario['role'] != 'admin':
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted", 200

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
