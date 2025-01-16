from bd import obtener_conexion
from clases import  claseFavorito as Favorito
from logger_config import logger
import mysql.connector

def insertar_favorito(producto_id, usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO favorito(producto_id, usuario_id, fecha_creacion) VALUES (%s, %s, NOW())"
            cursor.execute(sql, (producto_id, usuario_id))
            conexion.commit()

            favorito_id = cursor.lastrowid
            cursor.execute("SELECT id, fecha_creacion, producto_id, usuario_id FROM favorito WHERE id = %s", (favorito_id,))
            result = cursor.fetchone()
            if result:
                return Favorito(*result)
            else:
                logger.error(f"Error al obtener el favorito después de la inserción. ID: {favorito_id}")
                return None

    except mysql.connector.Error as e:
        logger.error(f"Error al insertar favorito: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_favoritos_por_usuario(usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha_creacion, producto_id, usuario_id FROM favorito WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            favoritos = [Favorito(*row) for row in cursor.fetchall()] #lista de objetos
        logger.info(f"Se obtuvieron {len(favoritos)} favoritos para el usuario {usuario_id}.")
        return favoritos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener favoritos del usuario {usuario_id}: {e}")
        return None #retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def verificar_favorito(producto_id, usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id FROM favorito WHERE producto_id = %s AND usuario_id = %s"
            cursor.execute(sql, (producto_id, usuario_id))
            favorito = cursor.fetchone()
        logger.info(f"Verificación de favorito para producto {producto_id} y usuario {usuario_id}: {'existe' if favorito else 'no existe'}.")
        return favorito is not None
    except mysql.connector.Error as e:
        logger.error(f"Error al verificar favorito: {e}")
        return None #retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def eliminar_favorito(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM favorito WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar favorito con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_favoritos_por_usuario(usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM favorito WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar favoritos del usuario {usuario_id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()