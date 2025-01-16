from flask import Flask,flash,render_template,request,jsonify,redirect,url_for,session
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
app.secret_key = "tu_clave_secreta" # ¡IMPORTANTE! Genera una clave secreta fuerte




@app.context_processor
def inject_user():
    # Suponiendo que usas Flask-Login
    from flask_login import current_user
    return {'user': current_user}


@app.route("/")
def home():
    productos_nuevos = controlador_producto.obtener_productos_nuevos()
    categorias = controlador_categoria.obtener_todas_categorias()
    return render_template('public/home.html', productos=productos_nuevos, categorias=categorias)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "Página de login en construcción"


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return "Página en construcción"


@app.route('/register', methods=['GET', 'POST'])
def register():
    return "Página de login en construcción"




@app.route('/carrito', methods=['GET', 'POST'])
def carrito():
    return "Página de login en construcción"



@app.route('/pago', methods=['GET', 'POST'])
def pago():
    return "Página de login en construcción"




@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    return "Página de login en construcción"




@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    return "Página de login en construcción"

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    return "Página de login en construcción"


@app.route('/about', methods=['GET', 'POST'])
def about():
    return "Página de login en construcción"

@app.route('/PoliticayPrivacidad', methods=['GET', 'POST'])
def PoliticayPrivacidad():
    return "Página de login en construcción"



@app.route('/TerminosyCondiciones', methods=['GET', 'POST'])
def TerminosyCondiciones():
    return "Página de login en construcción"

@app.route('/mis_compras',methods=['GET','POST'])
def mis_compras():
    return "Pagina en construccion"


@app.route('/mi_cuenta',methods=['GET','POST'])
def mi_cuenta():
    return "Pagina en construccion"




@app.route('/mis_favoritos',methods=['GET','POST'])
def mis_favoritos():
    return "Pagina en construccion"



@app.route('/mis_direcciones',methods=['GET','POST'])
def mis_direcciones():
    return "Pagina en construccion"


@app.route('/mis_metodos_pago',methods=['GET','POST'])
def mis_metodos_pago():
    return "Pagina en construccion"



# @app.route('/mi_cuenta',methods=['GET', 'POST'])
# def mi_cuenta():
#     return "Pagina en construccion"


#  ADMIN DASHBOARD
@app.route('/dashboard')
def dashboard():
    # usuarios=controlador_usuario.obtener_todos_usuarios()
    # pedidos=controlador_pedido.obtener_todos_pedidos()
    # categorias=controlador_categoria.obtener_todas_categorias()
    # return render_template('admin/dashboard.html',usuarios=usuarios,pedidos=pedidos,categorias=categorias)
    return render_template('/admin/dashboard.html')


@app.route('/admin_usuarios')
def admin_usuarios():
    usuarios= controlador_usuario.obtener_todos_usuarios()
    return render_template('admin/usuarios.html',usuarios=usuarios)


@app.route('/admin_productos')
def admin_productos():
    productos=controlador_producto.obtener_todos_productos()
    return render_template('admin/productos.html',productos=productos)



# INICIA CATEGORIAS
@app.route('/admin_categorias')
def admin_categorias():
    categorias=controlador_categoria.obtener_todas_categorias()
    return render_template('admin/categorias.html',categorias=categorias)

@app.route('/admin_agregar_categoria')
def admin_formulario_agregar_categoria():
    return render_template('admin/agregar_categoria.html')

@app.route('/admin_guardar_categoria',methods=['POST'])
def admin_guardar_categoria():
    nombre=request.form['nombre']
    controlador_categoria.insertar_categoria(nombre)
    flash('Categoría agregada', 'success')
    return redirect('/admin_categorias')

@app.route('/admin_eliminar_categoria',methods=['POST'])
def admin_eliminar_categoria():
    controlador_categoria.eliminar_categoria(request.form['id'])
    flash('Categoría eliminada', 'success')
    return redirect('/admin_categorias')

@app.route('/admin_editar_categoria/<int:id>')
def admin_formulario_editar_categoria(id):
    categoria=controlador_categoria.obtener_categoria_por_id(id)
    return render_template('admin/editar_categoria.html',categoria=categoria)

@app.route('/admin_actualizar_categoria',methods=['POST'])
def admin_actualizar_categoria():
    id=request.form['id']
    nombre=request.form['nombre']
    controlador_categoria.actualizar_categoria(id,nombre)
    flash('Categoría actualizada ', 'success')
    return redirect('/admin_categorias')
# FINALIZA CATEGORIAS 





@app.route('/admin_pedidos')
def admin_pedidos():
    pedidos=controlador_pedido.obtener_todos_pedidos
    return render_template('admin/pedidos.html',pedidos=pedidos)




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
# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     if not data or 'email' not in data or 'contrasena' not in data:
#         return jsonify({"error": "Credenciales inválidas"}), 400

#     email = data['email']
#     contrasena = data['contrasena']

#     usuario = verificar_contrasena(email, contrasena)

#     if usuario:
#         # Aquí implementarías la gestión de sesiones (ver abajo)
#         # Por ejemplo, usando Flask-Login o JWT
#         return jsonify({"mensaje": "Inicio de sesión exitoso", "usuario": usuario.to_dict()}), 200 #Retorna datos del usuario
#     else:
#         return jsonify({"error": "Credenciales inválidas"}), 401