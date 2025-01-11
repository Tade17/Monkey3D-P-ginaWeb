from bd import obtener_conexion
from logger_config import logger
from clases import claseUsuario
import mysql.connector
def insertar_usuario(usuario):
    if not isinstance(usuario, claseUsuario):
        logger.warning("Se debe proporcionar un objeto Usuario.")
        return False

    if not usuario.nombre or not usuario.nombre.strip() or not usuario.apellidos or not usuario.apellidos.strip() or not usuario.email or not usuario.email.strip() or not usuario.contrasena or not usuario.contrasena.strip():
        logger.warning("El nombre, apellidos, email y contraseña del usuario no pueden estar vacíos.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO usuario (nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (usuario.nombre, usuario.apellidos, usuario.email, usuario.contrasena, usuario.rol, usuario.foto, usuario.telefono, usuario.activo, usuario.fecha_registro))
        conexion.commit()
        usuario.id = cursor.lastrowid
        logger.info(f"Usuario '{usuario.nombre}' insertado exitosamente con ID: {usuario.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el usuario: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_usuarios():
    conexion = obtener_conexion()
    usuarios = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro FROM usuario"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                usuario = claseUsuario(*resultado)
                usuarios.append(usuario)
        logger.info(f"{len(usuarios)} usuarios obtenidos.")
        return usuarios
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuarios: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, apellidos, email, contrasena, rol, foto, telefono, activo, fecha_registro FROM usuario WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                usuario = claseUsuario(*resultado)
                logger.info(f"Usuario obtenido: {usuario}.")
        return usuario
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener usuario: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_usuario(usuario):
    if not isinstance(usuario, claseUsuario):
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
        logger.info(f"Usuario con id {usuario.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar usuario con id {usuario.id}: {e}")
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
        logger.info(f"Usuario con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar usuario con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()