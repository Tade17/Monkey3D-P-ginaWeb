from bd import obtener_conexion
from logger_config import logger
from clases import Usuario
import mysql.connector
import bcrypt

def insertar_usuario(usuario):
    if not isinstance(usuario, Usuario):
        logger.warning("Se debe proporcionar un objeto Usuario.")
        return None

    if not usuario.nombre or not usuario.nombre.strip() or not usuario.apellidos or not usuario.apellidos.strip() or not usuario.email or not usuario.email.strip() or not usuario.contrasena or not usuario.contrasena.strip():
        logger.warning("El nombre, apellidos, email y contraseña del usuario no pueden estar vacíos.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            hashed_password = bcrypt.hashpw(usuario.contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            sql = "INSERT INTO usuario (nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (usuario.nombre, usuario.apellidos, usuario.email, hashed_password, usuario.rol, usuario.foto, usuario.telefono, usuario.activo, usuario.fecha_registro))
            conexion.commit()

            usuario_id = cursor.lastrowid
            cursor.execute("SELECT id, nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro FROM usuario WHERE id = %s", (usuario_id,))
            result = cursor.fetchone()
            if result:
                return Usuario(*result)
            else:
                logger.error(f"Error al obtener el usuario después de la inserción. ID: {usuario_id}")
                return None

    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el usuario: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_usuarios():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro FROM usuario"
            cursor.execute(sql)
            usuarios = [Usuario(*row) for row in cursor.fetchall()]
        logger.info(f"{len(usuarios)} usuarios obtenidos.")
        return usuarios
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuarios: {e}")
        return None  # Retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro FROM usuario WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                usuario = Usuario(*resultado)
                logger.info(f"Usuario obtenido: {usuario}.")
                return usuario
            else:
                logger.warning(f"No se encontró un usuario con id {id}.")
                return None  # Retorna None si no se encuentra el usuario
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuario: {e}")
        return None  # Retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def actualizar_usuario(usuario):
    if not isinstance(usuario, Usuario):
        logger.warning("Se debe proporcionar un objeto Usuario.")
        return False
    if not usuario.nombre or not usuario.nombre.strip() or not usuario.apellidos or not usuario.apellidos.strip() or not usuario.email or not usuario.email.strip() or not usuario.contrasena or not usuario.contrasena.strip():
        logger.warning("El nombre, apellidos, email y contraseña del usuario no pueden estar vacíos.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE usuario SET nombre = %s, apellidos = %s, email = %s, contrasena = %s, rol = %s, foto = %s, telefono = %s, activo = %s, fecha_registro = %s WHERE id = %s"
            cursor.execute(sql, (usuario.nombre, usuario.apellidos, usuario.email, usuario.contrasena, usuario.rol, usuario.foto, usuario.telefono, usuario.activo, usuario.fecha_registro, usuario.id))
            conexion.commit()
            return cursor.rowcount > 0  # Retorna true si se actualizó al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar usuario con id {usuario.id}: {e}")
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
            return cursor.rowcount > 0  # Retorna true si se eliminó al menos una fila
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
            resultado = cursor.fetchone()
            if resultado:
                usuario = Usuario(*resultado)
                logger.info(f"Usuario obtenido: {usuario}.")
                return usuario
            else:
                logger.warning(f"No se encontró un usuario con email {email}.")
                return None  
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuario: {e}")
        return None  
    finally:
        if conexion:
            conexion.close()

def verificar_contrasena(email, contrasena_ingresada):
    usuario = obtener_usuario_por_email(email) #Necesitas crear esta función
    if usuario:
        if bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), usuario.contrasena.encode('utf-8')):
            return usuario  
        else:
            return None  
    else:
        return None  
            