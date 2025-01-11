from bd import obtener_conexion
from clases import claseFavorito
from logger_config import logger
import mysql.connector


def insertar_favorito(producto_id, usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO favorito(producto_id, usuario_id, fecha_creacion)
                VALUES (%s, %s, NOW())
                """,
                (producto_id, usuario_id)
            )
        conexion.commit()
        logger.info(f"Producto {producto_id} añadido a favoritos por el usuario {usuario_id}.")
    except Exception as e:
        logger.error(f"Error al insertar favorito: {e}")
        raise
    finally:
        conexion.close()

def obtener_favoritos_por_usuario(usuario_id):
    conexion = obtener_conexion()
    favoritos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, fecha_creacion, producto_id, usuario_id 
                FROM favorito 
                WHERE usuario_id = %s
                """,
                (usuario_id,)
            )
            favoritos = cursor.fetchall()
        logger.info(f"Se obtuvieron {len(favoritos)} favoritos para el usuario {usuario_id}.")
        return favoritos
    except Exception as e:
        logger.error(f"Error al obtener favoritos del usuario {usuario_id}: {e}")
        raise
    finally:
        conexion.close()

def verificar_favorito(producto_id, usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                SELECT id 
                FROM favorito 
                WHERE producto_id = %s AND usuario_id = %s
                """,
                (producto_id, usuario_id)
            )
            favorito = cursor.fetchone()
        logger.info(f"Verificación de favorito para producto {producto_id} y usuario {usuario_id}: {'existe' if favorito else 'no existe'}.")
        return favorito is not None
    except Exception as e:
        logger.error(f"Error al verificar favorito: {e}")
        raise
    finally:
        conexion.close()


def eliminar_favorito(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM favorito 
                WHERE id = %s
                """,
                (id,)
            )
        conexion.commit()
        logger.info(f"Favorito con id {id} eliminado.")
    except Exception as e:
        logger.error(f"Error al eliminar favorito con id {id}: {e}")
        raise
    finally:
        conexion.close()


def eliminar_favoritos_por_usuario(usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM favorito 
                WHERE usuario_id = %s
                """,
                (usuario_id,)
            )
        conexion.commit()
        logger.info(f"Todos los favoritos del usuario {usuario_id} fueron eliminados.")
    except Exception as e:
        logger.error(f"Error al eliminar favoritos del usuario {usuario_id}: {e}")
        raise
    finally:
        conexion.close()
