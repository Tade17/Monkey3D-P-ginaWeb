from bd import obtener_conexion
from clases import Notificaciones
from logger_config import logger
import mysql.connector

def insertar_notificacion(notificacion):
    if not isinstance(notificacion, Notificaciones):
        logger.warning("Se debe proporcionar un objeto Notificaciones.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO notificaciones (tipo, visto, usuario_id, pedido_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (notificacion.tipo, notificacion.visto, notificacion.usuario_id, notificacion.pedido_id))
            conexion.commit()

            notificacion_id = cursor.lastrowid
            cursor.execute("SELECT id, tipo, visto, fecha_creacion, usuario_id, pedido_id FROM notificaciones WHERE id = %s", (notificacion_id,))
            result = cursor.fetchone()
            if result:
                return Notificaciones(*result)
            else:
                logger.error(f"Error al obtener la notificación después de la inserción. ID: {notificacion_id}")
                return None

    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la notificación: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todas_notificaciones():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, tipo, visto, fecha_creacion, usuario_id, pedido_id FROM notificaciones"
            cursor.execute(sql)
            notificaciones = [Notificaciones(*row) for row in cursor.fetchall()]
        logger.info(f"{len(notificaciones)} notificaciones obtenidas.")
        return notificaciones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener notificaciones: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_notificaciones_por_usuario(usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, tipo, visto, fecha_creacion, usuario_id, pedido_id FROM notificaciones WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            notificaciones = [Notificaciones(*row) for row in cursor.fetchall()]
        logger.info(f"{len(notificaciones)} notificaciones obtenidas para el usuario con ID {usuario_id}.")
        return notificaciones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener notificaciones para el usuario con ID {usuario_id}: {e}")
        return None
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
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar el estado de la notificación con ID {notificacion_id}: {e}")
        if conexion:
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar la notificación con ID {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()