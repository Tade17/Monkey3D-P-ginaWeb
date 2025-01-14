from flask import Flask,render_template,request,jsonify,redirect,url_for,session
from controllers import (controlador_categoria,controlador_departamento,controlador_detallePedido,
                         controlador_direccion, controlador_distrito,controlador_domicilio,
                         controlador_favorito, controlador_metodo_pago,controlador_notificaciones,
                         controlador_opiniones,controlador_pago,controlador_pedido,controlador_producto,
                         controlador_provincias,controlador_usuario)

from flask_login import current_user
import bcrypt
import jwt
from datetime import datetime, timedelta
import os 






app=Flask(__name__)

@app.context_processor
def inject_user():
    # Suponiendo que usas Flask-Login
    from flask_login import current_user
    return {'user': current_user}


@app.route("/")
def home():
    productos_destacados = controlador_producto.obtener_productos_destacados()
    categorias = controlador_categoria.obtener_todas_categorias()
    return render_template("public/index.html", productos=productos_destacados, categorias=categorias)
    
if __name__ == '__main__':
    app.run(debug=True)




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/login")
def login():
    return render_template("/public/login.html")










@app.route("/main")
def main():
    return render_template("/public/index.html")

@app.route("/dashboard")
def login_admin():
    return render_template("/admin/dashboard.html")



































#APIS PA 
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'contrasena' not in data:
        return jsonify({"error": "Credenciales inválidas"}), 400

    email = data['email']
    contrasena = data['contrasena']

    usuario = verificar_contrasena(email, contrasena)

    if usuario:
        # Aquí implementarías la gestión de sesiones (ver abajo)
        # Por ejemplo, usando Flask-Login o JWT
        return jsonify({"mensaje": "Inicio de sesión exitoso", "usuario": usuario.to_dict()}), 200 #Retorna datos del usuario
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401