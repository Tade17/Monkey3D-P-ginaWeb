from bd import obtener_conexion
from clases import claseProvincia 
from logger_config import logger
import mysql.connector
def insertar_provincia(provincia):
    if not isinstance(provincia, claseProvincia):
        logger.warning("Se debe proporcionar un objeto Provincia.")
        return False

    if not provincia.nombre or not provincia.nombre.strip():
        logger.warning("El nombre de la provincia está vacío o es inválido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO provincia (nombre, disponible, fecha_creacion, departamento_id, codigo_postal) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (provincia.nombre, provincia.disponible, provincia.fecha_creacion, provincia.departamento_id, provincia.codigo_postal))
        conexion.commit()
        provincia.id = cursor.lastrowid
        logger.info(f"Provincia '{provincia.nombre}' insertada exitosamente con ID: {provincia.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la provincia '{provincia.nombre}': {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todas_provincias():
    conexion = obtener_conexion()
    provincias = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, disponible, fecha_creacion, departamento_id, codigo_postal FROM provincia"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                provincia = claseProvincia(*resultado)
                provincias.append(provincia)
        logger.info(f"{len(provincias)} provincias obtenidas.")
        return provincias
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener provincias: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_provincia_por_id(id):
    conexion = obtener_conexion()
    provincia = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, disponible, fecha_creacion, departamento_id, codigo_postal FROM provincia WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                provincia = claseProvincia(*resultado)
                logger.info(f"Provincia obtenida: {provincia}.")
        return provincia
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener provincia: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_provincia(provincia):
    if not isinstance(provincia, claseProvincia):
        logger.warning("Se debe proporcionar un objeto Provincia.")
        return False

    if not provincia.nombre or not provincia.nombre.strip():
        logger.warning("El nombre de la provincia está vacío o es inválido.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE provincia SET nombre = %s, disponible = %s, codigo_postal = %s, departamento_id = %s WHERE id = %s"
            cursor.execute(sql, (provincia.nombre, provincia.disponible, provincia.codigo_postal, provincia.departamento_id, provincia.id))
        conexion.commit()
        logger.info(f"Provincia con id {provincia.id} actualizada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar provincia con id {provincia.id}: {e}")
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
        logger.info(f"Provincia con id {id} eliminada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar provincia con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()