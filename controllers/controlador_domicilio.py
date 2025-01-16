from bd import obtener_conexion
from logger_config import logger
from clases import claseDomicilio as  Domicilio
import mysql.connector

def insertar_domicilio(domicilio):
    if not isinstance(domicilio, Domicilio):
        logger.warning("Se debe proporcionar un objeto Domicilio.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO domicilio (predeterminado, fecha_creacion, direccion_id, usuario_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (domicilio.predeterminado, domicilio.fecha_creacion, domicilio.direccion_id, domicilio.usuario_id))
            conexion.commit()

            domicilio_id = cursor.lastrowid
            cursor.execute("SELECT id, predeterminado, fecha_creacion, direccion_id, usuario_id FROM domicilio WHERE id = %s", (domicilio_id,))
            result = cursor.fetchone()
            if result:
                return Domicilio(*result)
            else:
                logger.error(f"Error al obtener el domicilio después de la inserción. ID: {domicilio_id}")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el domicilio: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_domicilios():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, predeterminado, fecha_creacion, direccion_id, usuario_id FROM domicilio"
            cursor.execute(sql)
            domicilios = [Domicilio(*row) for row in cursor.fetchall()]
        logger.info(f"{len(domicilios)} domicilios obtenidos.")
        return domicilios
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener domicilios: {e}")
        return None #retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def obtener_domicilio_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, predeterminado, fecha_creacion, direccion_id, usuario_id FROM domicilio WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                domicilio = Domicilio(*resultado)
                logger.info(f"Domicilio obtenido: {domicilio}.")
                return domicilio
            else:
                logger.warning(f"No se encontró un domicilio con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener domicilio: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_domicilio(domicilio):
    if not isinstance(domicilio, Domicilio):
        logger.warning("Se debe proporcionar un objeto Domicilio.")
        return False #Puedes dejarlo asi para tu logica
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE domicilio SET predeterminado = %s, fecha_creacion = %s, direccion_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (domicilio.predeterminado, domicilio.fecha_creacion, domicilio.direccion_id, domicilio.usuario_id, domicilio.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar domicilio con id {domicilio.id}: {e}")
        if conexion:
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar domicilio con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()