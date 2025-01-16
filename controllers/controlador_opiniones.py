from bd import obtener_conexion
from logger_config import logger
from clases import claseOpiniones as Opiniones  # Importa la clase con el nombre correcto
import mysql.connector

def insertar_opinion(opinion):
    if not isinstance(opinion, Opiniones):
        logger.warning("Se debe proporcionar un objeto Opiniones.")
        return None

    if not opinion.resena or not opinion.resena.strip() or opinion.calificacion is None or not 1 <= opinion.calificacion <= 5:
        logger.warning("La reseña no puede estar vacía y la calificación debe estar entre 1 y 5.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO opiniones (resena, calificacion, fecha_creacion, producto_id, usuario_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (opinion.resena, opinion.calificacion, opinion.fecha_creacion, opinion.producto_id, opinion.usuario_id))
            conexion.commit()

            opinion_id = cursor.lastrowid
            cursor.execute("SELECT id, resena, calificacion, fecha_creacion, producto_id, usuario_id FROM opiniones WHERE id = %s", (opinion_id,))
            result = cursor.fetchone()
            if result:
                return Opiniones(*result)
            else:
                logger.error(f"Error al obtener la opinión después de la inserción. ID: {opinion_id}")
                return None

    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la opinión: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todas_opiniones():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, resena, calificacion, fecha_creacion, producto_id, usuario_id FROM opiniones"
            cursor.execute(sql)
            opiniones = [Opiniones(*row) for row in cursor.fetchall()]
        logger.info(f"{len(opiniones)} opiniones obtenidas.")
        return opiniones
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener opiniones: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_opinion_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, resena, calificacion, fecha_creacion, producto_id, usuario_id FROM opiniones WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                opinion = Opiniones(*resultado)
                logger.info(f"Opinión obtenida: {opinion}.")
                return opinion
            else:
                logger.warning(f"No se encontró una opinión con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener opinión: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_opinion(opinion):
    if not isinstance(opinion, Opiniones):
        logger.warning("Se debe proporcionar un objeto Opiniones.")
        return False #Puedes dejarlo asi para tu logica
    if not opinion.resena or not opinion.resena.strip() or opinion.calificacion is None or not 1 <= opinion.calificacion <= 5:
        logger.warning("La reseña no puede estar vacía y la calificación debe estar entre 1 y 5.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE opiniones SET resena = %s, calificacion = %s, fecha_creacion = %s, producto_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (opinion.resena, opinion.calificacion, opinion.fecha_creacion, opinion.producto_id, opinion.usuario_id, opinion.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar opinión con id {opinion.id}: {e}")
        if conexion:
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar opinión con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()