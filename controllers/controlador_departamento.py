from bd import obtener_conexion
from clases import claseDepartamento
from logger_config import logger
import mysql.connector

def insertar_departamento(departamento):
    if not departamento.nombre or not departamento.nombre.strip():
        logger.warning("El nombre del departamento está vacío o es inválido.")
        return False
    if not departamento.codigo_postal or not str(departamento.codigo_postal).isdigit():
        logger.warning("El código postal está vacío o es inválido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO departamento (nombre, codigo_postal) VALUES (%s, %s)"
            cursor.execute(sql, (departamento.nombre, departamento.codigo_postal))
        conexion.commit()
        departamento.id = cursor.lastrowid 
        logger.info(f"Departamento '{departamento.nombre}' insertado exitosamente con ID: {departamento.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el departamento '{departamento.nombre}': {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_departamentos():
    conexion = obtener_conexion()
    departamentos = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, codigo_postal, disponible, fecha_creacion FROM departamento"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                departamento = claseDepartamento(*resultado)
                departamentos.append(departamento)
        logger.info(f"{len(departamentos)} departamentos obtenidos.")
        return departamentos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener departamentos: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_departamento_por_id(id):
    conexion = obtener_conexion()
    departamento = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, codigo_postal, disponible, fecha_creacion FROM departamento WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                departamento =claseDepartamento(*resultado)
                logger.info(f"Departamento obtenido: {departamento}.")
            else:
                logger.warning(f"No se encontró un departamento con id {id}.")
        return departamento
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener departamento: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_departamento(departamento):

    if not departamento.nombre or not departamento.nombre.strip():
        logger.warning("El nombre del departamento está vacío o es inválido.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE departamento SET nombre = %s, codigo_postal = %s, disponible = %s WHERE id = %s"
            cursor.execute(sql, (departamento.nombre, departamento.codigo_postal, departamento.disponible, departamento.id))
        conexion.commit()
        logger.info(f"Departamento con id {departamento.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar departamento con id {departamento.id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_departamento(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql_check = "SELECT COUNT(*) FROM provincia WHERE departamento_id = %s"
            cursor.execute(sql_check, (id,))
            count = cursor.fetchone()[0]
            if count > 0:
                logger.warning(f"No se puede eliminar el departamento con id {id}: tiene {count} provincia(s) asociada(s).")
                return False

            sql = "DELETE FROM departamento WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Departamento con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar departamento con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()