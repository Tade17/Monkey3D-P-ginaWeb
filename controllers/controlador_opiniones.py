from bd import obtener_conexion
from logger_config import logger
from clases import claseOpiniones
import mysql.connector

def insertar_opinion(opinion):
    if not isinstance(opinion, claseOpiniones):
        logger.warning("Se debe proporcionar un objeto Opiniones.")
        return False
    if not opinion.resena or not opinion.resena.strip() or opinion.calificacion is None or not 1 <= opinion.calificacion <= 5: #validacion de calificacion entre 1 y 5
        logger.warning("La reseña no puede estar vacía y la calificación debe estar entre 1 y 5")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO opiniones (resena, calificacion, fecha_creacion, producto_id, usuario_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (opinion.resena, opinion.calificacion, opinion.fecha_creacion, opinion.producto_id, opinion.usuario_id))
        conexion.commit()
        opinion.id = cursor.lastrowid
        logger.info(f"Opinión insertada exitosamente con ID: {opinion.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la opinión: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todas_opiniones():
    conexion = obtener_conexion()
    opiniones = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, resena, calificacion, fecha_creacion, producto_id, usuario_id FROM opiniones"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                opinion = claseOpiniones(*resultado)
                opiniones.append(opinion)
        logger.info(f"{len(opiniones)} opiniones obtenidas.")
        return opiniones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener opiniones: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_opinion_por_id(id):
    conexion = obtener_conexion()
    opinion = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, resena, calificacion, fecha_creacion, producto_id, usuario_id FROM opiniones WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                opinion = claseOpiniones(*resultado)
                logger.info(f"Opinión obtenida: {opinion}.")
        return opinion
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener opinión: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_opinion(opinion):
    if not isinstance(opinion, claseOpiniones):
        logger.warning("Se debe proporcionar un objeto Opiniones.")
        return False
    if not opinion.resena or not opinion.resena.strip() or opinion.calificacion is None or not 1 <= opinion.calificacion <= 5: #validacion de calificacion entre 1 y 5
        logger.warning("La reseña no puede estar vacía y la calificación debe estar entre 1 y 5")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE opiniones SET resena = %s, calificacion = %s, fecha_creacion = %s, producto_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (opinion.resena, opinion.calificacion, opinion.fecha_creacion, opinion.producto_id, opinion.usuario_id, opinion.id))
        conexion.commit()
        logger.info(f"Opinión con id {opinion.id} actualizada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar opinión con id {opinion.id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_opinion(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM opiniones WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Opinión con id {id} eliminada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar opinión con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()