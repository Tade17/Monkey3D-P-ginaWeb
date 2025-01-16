from bd import obtener_conexion
from logger_config import logger
from clases import claseUsuario 
import mysql.connector
import bcrypt

def insertar_usuario(nombre,apellidos,email,contrasena,rol,foto,telefono):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            sql = "INSERT INTO usuario (nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, apellidos, email, hashed_password, rol, foto, telefono))
            conexion.commit()
            usuario_id = cursor.lastrowid
            cursor.execute("SELECT id, nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro FROM usuario WHERE id = %s", (usuario_id,))
            return f"Usuario ingresado con id:{usuario_id}"           
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el usuario: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_usuarios():
    conexion=obtener_conexion()
    usuarios=[]
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                select id,nombre,apellidos,email,rol,telefono,activo
                from usuario     
                """
            )
            usuarios=cursor.fetchall()
        logger.info("Usuarios obtenidos correctamente")
        return usuarios
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuarios{e}")
        if conexion:
            conexion.close()
        return False
    finally:
        if conexion:
            conexion.close()
           
def obtener_usuario_por_id(id):
    conexion=obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
            """
            select id,nombre,apellidos,email,contrasena,rol,foto,telefono,activo,fecha_creacion
            from usuario 
            where id=%s
            """,(id,)
            )
        usuario=cursor.fetchone()
        return usuario   
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuario con id{id} : {e}")
        return False
    finally:
        if conexion:
            conexion.close()

def actualizar_usuario(id,nombre,apellidos,email,contrasena,rol,foto,telefono,activo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE usuario SET nombre = %s, apellidos = %s, email = %s, contrasena = %s, rol = %s, foto = %s, telefono = %s, activo = %s WHERE id = %s"
            cursor.execute(sql, (id,nombre,apellidos,email,contrasena,rol,foto,telefono,activo))
            conexion.commit()
            return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar usuario con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_usuario(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM usuario WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
            return True # Retorna true si se eliminó al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar usuario con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()
            
            
# para el login 

def obtener_usuario_por_email(email):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro FROM usuario WHERE email = %s"
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()
        logger.info("Usuario obtenido")
        return usuario  
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuario: {e}")
        return None  
    finally:
        if conexion:
            conexion.close()


def verificar_contrasena(email, contrasena_ingresada):
    usuario = obtener_usuario_por_email(email) 
    if usuario:
        if bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), usuario.contrasena.encode('utf-8')):
            return usuario  
        else:
            return None  
    else:
        return None  
            