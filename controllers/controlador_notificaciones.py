from bd import obtener_conexion
from clases import claseNotificaciones
from logger_config import logger
import mysql.connector


def insertar_notificacion(notificacion):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO notificaciones (tipo, visto, usuario_id, pedido_id)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (notificacion.tipo, notificacion.visto, notificacion.usuario_id, notificacion.pedido_id))
        conexion.commit()
        notificacion.id = cursor.lastrowid
        logger.info(f"Notificación '{notificacion.tipo}' insertada con ID: {notificacion.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la notificación: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()


def obtener_todas_notificaciones():
    conexion = obtener_conexion()
    notificaciones = []
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, tipo, visto, fecha_creacion, usuario_id, pedido_id
                FROM notificaciones
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                notificacion = claseNotificaciones(*resultado)
                notificaciones.append(notificacion)
        logger.info(f"{len(notificaciones)} notificaciones obtenidas.")
        return notificaciones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener notificaciones: {e}")
        return []
    finally:
        if conexion:
            conexion.close()
 
def obtener_notificaciones_por_usuario(usuario_id):
    conexion = obtener_conexion()
    notificaciones = []
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, tipo, visto, fecha_creacion, usuario_id, pedido_id
                FROM notificaciones
                WHERE usuario_id = %s
            """
            cursor.execute(sql, (usuario_id,))
            resultados = cursor.fetchall()
            for resultado in resultados:
                notificacion = claseNotificaciones(*resultado)
                notificaciones.append(notificacion)
        logger.info(f"{len(notificaciones)} notificaciones obtenidas para el usuario con ID {usuario_id}.")
        return notificaciones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener notificaciones para el usuario con ID {usuario_id}: {e}")
        return []
    finally:
        if conexion:
            conexion.close()


def actualizar_estado_visto(notificacion_id, visto=True):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE notificaciones SET visto = %s WHERE id = %s"
            cursor.execute(sql, (visto, notificacion_id))
        conexion.commit()
        logger.info(f"Notificación con ID {notificacion_id} actualizada a visto={visto}.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar el estado de la notificación con ID {notificacion_id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()


def eliminar_notificacion(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM notificaciones WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Notificación con ID {id} eliminada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar la notificación con ID {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()


