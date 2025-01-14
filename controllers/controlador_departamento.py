from bd import obtener_conexion
from clases import Departamento
from logger_config import logger
import mysql.connector

def insertar_departamento(departamento):
    if not departamento.codigo_postal or not str(departamento.codigo_postal).isdigit():
        logger.warning("El código postal está vacío o es inválido.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO departamento (nombre, codigo_postal, disponible) VALUES (%s, %s, %s)" #Agrego el campo disponible
            cursor.execute(sql, (departamento.nombre, departamento.codigo_postal, departamento.disponible)) #agrego el campo disponible
            conexion.commit()
            departamento_id = cursor.lastrowid
            cursor.execute("SELECT id, nombre, codigo_postal, disponible, fecha_creacion FROM departamento WHERE id = %s", (departamento_id,))
            result = cursor.fetchone()
            if result:
                return Departamento(*result)
            else:
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el departamento '{departamento.nombre}': {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_departamentos():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, codigo_postal, disponible, fecha_creacion FROM departamento"
            cursor.execute(sql)
            departamentos = [Departamento(*row) for row in cursor.fetchall()]
        logger.info(f"{len(departamentos)} departamentos obtenidos.")
        return departamentos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener departamentos: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_departamento_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, codigo_postal, disponible, fecha_creacion FROM departamento WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                departamento = Departamento(*resultado)
                logger.info(f"Departamento obtenido: {departamento}.")
                return departamento
            else:
                logger.warning(f"No se encontró un departamento con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener departamento: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_departamento(departamento):
    if not departamento.nombre or not departamento.nombre.strip():
        logger.warning("El nombre del departamento está vacío o es inválido.")
        return False #puedes dejarlo asi para tu logica
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE departamento SET nombre = %s, codigo_postal = %s, disponible = %s WHERE id = %s"
            cursor.execute(sql, (departamento.nombre, departamento.codigo_postal, departamento.disponible, departamento.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar departamento con id {departamento.id}: {e}")
        if conexion:
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar departamento con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()