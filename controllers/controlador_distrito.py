from bd import obtener_conexion
from logger_config import logger
from clases import claseDistrito as Distrito
import mysql.connector

def insertar_distrito(distrito):
    if not isinstance(distrito, Distrito):
        logger.warning("Se debe proporcionar un objeto Distrito.")
        return None

    if not distrito.nombre or not distrito.nombre.strip():
        logger.warning("El nombre del distrito está vacío o es inválido.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO distrito (nombre, disponible, fecha_creacion, provincia_id, codigo_postal) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (distrito.nombre, distrito.disponible, distrito.fecha_creacion, distrito.provincia_id, distrito.codigo_postal))
            conexion.commit()

            distrito_id = cursor.lastrowid
            cursor.execute("SELECT id, nombre, disponible, fecha_creacion, provincia_id, codigo_postal FROM distrito WHERE id = %s", (distrito_id,))
            result = cursor.fetchone()
            if result:
                return Distrito(*result)
            else:
                logger.error(f"Error al obtener el distrito después de la inserción. ID: {distrito_id}")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el distrito: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_distritos():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, disponible, fecha_creacion, provincia_id, codigo_postal FROM distrito"
            cursor.execute(sql)
            distritos = [Distrito(*row) for row in cursor.fetchall()]
        logger.info(f"{len(distritos)} distritos obtenidos.")
        return distritos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener distritos: {e}")
        return None #Retornar None en caso de error
    finally:
        if conexion:
            conexion.close()

def obtener_distrito_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, disponible, fecha_creacion, provincia_id, codigo_postal FROM distrito WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                distrito = Distrito(*resultado)
                logger.info(f"Distrito obtenido: {distrito}.")
                return distrito
            else:
                logger.warning(f"No se encontró un distrito con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener distrito: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_distrito(distrito):
    if not isinstance(distrito, Distrito):
        logger.warning("Se debe proporcionar un objeto Distrito.")
        return False #puedes dejarlo asi para tu logica
    if not distrito.nombre or not distrito.nombre.strip():
        logger.warning("El nombre del distrito está vacío o es inválido.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE distrito SET nombre = %s, disponible = %s, codigo_postal = %s, provincia_id = %s WHERE id = %s"
            cursor.execute(sql, (distrito.nombre, distrito.disponible, distrito.codigo_postal, distrito.provincia_id, distrito.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar distrito con id {distrito.id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_distrito(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM distrito WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar distrito con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()