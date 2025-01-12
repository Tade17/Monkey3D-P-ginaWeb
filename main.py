from flask import Flask,render_template,request
from controllers import (controlador_categoria,controlador_departamento,controlador_detallePedido,
                         controlador_direccion, controlador_distrito,controlador_domicilio,
                         controlador_favorito, controlador_metodo_pago,controlador_notificaciones,
                         controlador_opiniones,controlador_pago,controlador_pedido,controlador_producto,
                         controlador_provincias,controlador_usuario)

from flask_login import current_user







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
