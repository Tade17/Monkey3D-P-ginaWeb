from bd import obtener_conexion
from clases import clasePais  # Import the clasePais class
from logger_config import logger
import mysql.connector

def obtener_todos_paises():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, codigo_iso, disponible, fecha_creacion FROM pais") #added fecha_creacion
            paises = []
            for row in cursor.fetchall():
                paises.append(clasePais(*row))  # Create clasePais objects from each row
        return paises
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener paises: {e}")
        return None  # Or return a more structured error
    finally:
        if conexion:
            conexion.close()

def obtener_pais_por_id(id):  # Changed function name for clarity
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, codigo_iso, disponible, fecha_creacion FROM pais WHERE id = %s", (id,)) #added fecha_creacion
            result = cursor.fetchone()  # Fetch a single result
            if result:
                return clasePais(*result)  # Create and return a clasePais object
            else:
                return None  # Return None if no country is found
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pais con ID {id}: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def insertar_pais(nombre, codigo_iso):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO pais (nombre, codigo_iso) VALUES (%s, %s)", (nombre, codigo_iso))
            conexion.commit()
            return cursor.lastrowid # Return the ID of the inserted row
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el pais {nombre}: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def dar_de_baja_pais(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE pais SET disponible = 0 WHERE id = %s", (id,))
            conexion.commit()
            return cursor.rowcount > 0 # Return True if at least one row was updated
    except mysql.connector.Error as e:
        logger.error(f"No se pudo dar de baja al pais con ID {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_pais(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM pais WHERE id = %s", (id,))
            conexion.commit()
            return cursor.rowcount > 0 # Return True if at least one row was deleted
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar pais con ID {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()