from bd import obtener_conexion
from logger_config import logger
from clases import claseDireccion
import mysql.connector

def insertar_direccion(direccion):
    if not isinstance(direccion, claseDireccion):
        logger.warning("Se debe proporcionar un objeto Direccion.")
        return False

    if not direccion.calle or not direccion.calle.strip() or not direccion.numero_casa or not direccion.numero_casa.strip():
        logger.warning("La calle y el número de casa no pueden estar vacíos.")
        return False
        
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO direccion (calle, numero_casa, referencia, fecha_creacion, distrito_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (direccion.calle, direccion.numero_casa, direccion.referencia, direccion.fecha_creacion, direccion.distrito_id))
        conexion.commit()
        direccion.id = cursor.lastrowid
        logger.info(f"Dirección insertada exitosamente con ID: {direccion.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la dirección: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todas_direcciones():
    conexion = obtener_conexion()
    direcciones = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, calle, numero_casa, referencia, fecha_creacion, distrito_id FROM direccion"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                direccion = claseDireccion(*resultado)
                direcciones.append(direccion)
        logger.info(f"{len(direcciones)} direcciones obtenidas.")
        return direcciones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener direcciones: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_direccion_por_id(id):
    conexion = obtener_conexion()
    direccion = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, calle, numero_casa, referencia, fecha_creacion, distrito_id FROM direccion WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                direccion = claseDireccion(*resultado)
                logger.info(f"Dirección obtenida: {direccion}.")
        return direccion
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener dirección: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_direccion(direccion):
    if not isinstance(direccion, claseDireccion):
        logger.warning("Se debe proporcionar un objeto Direccion.")
        return False
    if not direccion.calle or not direccion.calle.strip() or not direccion.numero_casa or not direccion.numero_casa.strip():
        logger.warning("La calle y el número de casa no pueden estar vacíos.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE direccion SET calle = %s, numero_casa = %s, referencia = %s, fecha_creacion = %s, distrito_id = %s WHERE id = %s"
            cursor.execute(sql, (direccion.calle, direccion.numero_casa, direccion.referencia, direccion.fecha_creacion, direccion.distrito_id, direccion.id))
        conexion.commit()
        logger.info(f"Dirección con id {direccion.id} actualizada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar dirección con id {direccion.id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_direccion(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM direccion WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Dirección con id {id} eliminada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar dirección con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()