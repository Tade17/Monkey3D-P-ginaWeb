from bd import obtener_conexion
from logger_config import logger
from clases import claseProvincia as Provincia
import mysql.connector
11
def insertar_provincia(nombre,departamento_id,codigo_postal):

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
            INSERT INTO provincia (nombre,codigo_postal,departamento_id) VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (nombre,codigo_postal,departamento_id))
            conexion.commit()
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la provincia '{nombre}': {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todas_provincias():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
            SELECT id, nombre, disponible,codigo_postal,fecha_creacion, departamento_id,  FROM provincia
            """
            cursor.execute(sql)
            provincias = [Provincia(*row) for row in cursor.fetchall()]
        logger.info(f"{len(provincias)} provincias obtenidas.")
        return provincias
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener provincias: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_provincia_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """SELECT id, nombre, disponible,codigo_postal,fecha_creacion,departamento_id
             FROM provincia WHERE id = %s
             """
            cursor.execute(sql, (id,))
            provincia=cursor.fetchone()
        logger.info("Provincia obtenida")        
        return provincia  
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener provincia: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_provincia(id,nombre,disponible,codigo_postal):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE provincia SET nombre = %s, disponible = %s, codigo_postal = %s, departamento_id = %s WHERE id = %s"
            cursor.execute(sql, (id,nombre,disponible,codigo_postal))
            conexion.commit()
            return True 
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar provincia con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_provincia(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql_check = "SELECT COUNT(*) FROM distrito WHERE provincia_id = %s"
            cursor.execute(sql_check, (id,))
            count = cursor.fetchone()[0]
            if count > 0:
                logger.warning(f"No se puede eliminar la provincia con id {id}: tiene {count} distrito(s) asociado(s).")
                return False

            sql = "DELETE FROM provincia WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
            logger.info(f"Se eliminó la provincia con id: {id}")
            return True #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar provincia con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()