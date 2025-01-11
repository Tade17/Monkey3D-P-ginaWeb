from bd import obtener_conexion
from logger_config import logger
from clases import claseDomicilio
import mysql.connector
def insertar_domicilio(domicilio):
    if not isinstance(domicilio, claseDomicilio):
        logger.warning("Se debe proporcionar un objeto Domicilio.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO domicilio (predeterminado, fecha_creacion, direccion_id, usuario_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (domicilio.predeterminado, domicilio.fecha_creacion, domicilio.direccion_id, domicilio.usuario_id))
        conexion.commit()
        domicilio.id = cursor.lastrowid
        logger.info(f"Domicilio insertado exitosamente con ID: {domicilio.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el domicilio: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_domicilios():
    conexion = obtener_conexion()
    domicilios = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, predeterminado, fecha_creacion, direccion_id, usuario_id FROM domicilio"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                domicilio = claseDomicilio(*resultado)
                domicilios.append(domicilio)
        logger.info(f"{len(domicilios)} domicilios obtenidos.")
        return domicilios
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener domicilios: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_domicilio_por_id(id):
    conexion = obtener_conexion()
    domicilio = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, predeterminado, fecha_creacion, direccion_id, usuario_id FROM domicilio WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                domicilio = claseDomicilio(*resultado)
                logger.info(f"Domicilio obtenido: {domicilio}.")
        return domicilio
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener domicilio: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_domicilio(domicilio):
    if not isinstance(domicilio, claseDomicilio):
        logger.warning("Se debe proporcionar un objeto Domicilio.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE domicilio SET predeterminado = %s, fecha_creacion = %s, direccion_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (domicilio.predeterminado, domicilio.fecha_creacion, domicilio.direccion_id, domicilio.usuario_id, domicilio.id))
        conexion.commit()
        logger.info(f"Domicilio con id {domicilio.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar domicilio con id {domicilio.id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_domicilio(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM domicilio WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Domicilio con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar domicilio con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()