from bd import obtener_conexion
from logger_config import logger
from clases import claseDireccion as Direccion # Importa la clase correctamente
import mysql.connector

def insertar_direccion(direccion):
    if not isinstance(direccion, Direccion):
        logger.warning("Se debe proporcionar un objeto Direccion.")
        return None

    if not direccion.calle or not direccion.calle.strip() or not direccion.numero_casa or not str(direccion.numero_casa).strip(): #convierte a string por si es un int
        logger.warning("La calle y el número de casa no pueden estar vacíos.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO direccion (calle, numero_casa, referencia, fecha_creacion, distrito_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (direccion.calle, direccion.numero_casa, direccion.referencia, direccion.fecha_creacion, direccion.distrito_id))
            conexion.commit()

            direccion_id = cursor.lastrowid
            cursor.execute("SELECT id, calle, numero_casa, referencia, fecha_creacion, distrito_id FROM direccion WHERE id = %s", (direccion_id,))
            result = cursor.fetchone()
            if result:
                return Direccion(*result)
            else:
                logger.error(f"Error al obtener la dirección después de la inserción. ID: {direccion_id}")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la dirección: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todas_direcciones():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, calle, numero_casa, referencia, fecha_creacion, distrito_id FROM direccion"
            cursor.execute(sql)
            direcciones = [Direccion(*row) for row in cursor.fetchall()]
        logger.info(f"{len(direcciones)} direcciones obtenidas.")
        return direcciones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener direcciones: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_direccion_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, calle, numero_casa, referencia, fecha_creacion, distrito_id FROM direccion WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                direccion = Direccion(*resultado)
                logger.info(f"Dirección obtenida: {direccion}.")
                return direccion
            else:
                logger.warning(f"No se encontró una dirección con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener dirección: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_direccion(direccion):
    if not isinstance(direccion, Direccion):
        logger.warning("Se debe proporcionar un objeto Direccion.")
        return False #puedes dejarlo asi para tu logica
    if not direccion.calle or not direccion.calle.strip() or not direccion.numero_casa or not str(direccion.numero_casa).strip(): #convierte a string por si es un int
        logger.warning("La calle y el número de casa no pueden estar vacíos.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE direccion SET calle = %s, numero_casa = %s, referencia = %s, fecha_creacion = %s, distrito_id = %s WHERE id = %s"
            cursor.execute(sql, (direccion.calle, direccion.numero_casa, direccion.referencia, direccion.fecha_creacion, direccion.distrito_id, direccion.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar dirección con id {direccion.id}: {e}")
        if conexion:
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar dirección con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()