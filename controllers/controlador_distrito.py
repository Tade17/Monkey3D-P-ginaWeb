from bd import obtener_conexion
from logger_config import logger
from clases import claseDistrito
import mysql.connector
def insertar_distrito(distrito):
    if not isinstance(distrito, claseDistrito):
        logger.warning("Se debe proporcionar un objeto Distrito.")
        return False

    if not distrito.nombre or not distrito.nombre.strip():
        logger.warning("El nombre del distrito está vacío o es inválido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO distrito (nombre, disponible, fecha_creacion, provincia_id, codigo_postal) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (distrito.nombre, distrito.disponible, distrito.fecha_creacion, distrito.provincia_id, distrito.codigo_postal))
        conexion.commit()
        distrito.id = cursor.lastrowid
        logger.info(f"Distrito '{distrito.nombre}' insertado exitosamente con ID: {distrito.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el distrito: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_distritos():
    conexion = obtener_conexion()
    distritos = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, disponible, fecha_creacion, provincia_id, codigo_postal FROM distrito"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                distrito = claseDistrito(*resultado)
                distritos.append(distrito)
        logger.info(f"{len(distritos)} distritos obtenidos.")
        return distritos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener distritos: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_distrito_por_id(id):
    conexion = obtener_conexion()
    distrito = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, disponible, fecha_creacion, provincia_id, codigo_postal FROM distrito WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                distrito = claseDistrito(*resultado)
                logger.info(f"Distrito obtenido: {distrito}.")
        return distrito
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener distrito: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_distrito(distrito):
    if not isinstance(distrito, claseDistrito):
        logger.warning("Se debe proporcionar un objeto Distrito.")
        return False

    if not distrito.nombre or not distrito.nombre.strip():
        logger.warning("El nombre del distrito está vacío o es inválido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE distrito SET nombre = %s, disponible = %s, codigo_postal = %s, provincia_id = %s WHERE id = %s"
            cursor.execute(sql, (distrito.nombre, distrito.disponible, distrito.codigo_postal, distrito.provincia_id, distrito.id))
        conexion.commit()
        logger.info(f"Distrito con id {distrito.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar distrito con id {distrito.id}: {e}")
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
        logger.info(f"Distrito con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar distrito con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()