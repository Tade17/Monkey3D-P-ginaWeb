from bd import obtener_conexion
from clases import claseMetodoPago
from logger_config import logger
import mysql.connector

def insertar_metodo_pago(metodo_pago):
    if not metodo_pago.nombre_metodo_pago or not metodo_pago.nombre_metodo_pago.strip():
        logger.warning("El nombre del método de pago está vacío o es inválido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO metodo_pago (nombre_metodo_pago, numero_tarjeta, cvv, titular, predeterminado, 
                                         fecha_vencimiento, usuario_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (metodo_pago.nombre_metodo_pago, metodo_pago.numero_tarjeta, metodo_pago.cvv,
                                 metodo_pago.titular, metodo_pago.predeterminado, metodo_pago.fecha_vencimiento,
                                 metodo_pago.usuario_id))
        conexion.commit()
        metodo_pago.id = cursor.lastrowid
        logger.info(f"Método de pago '{metodo_pago.nombre_metodo_pago}' insertado exitosamente con ID: {metodo_pago.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el método de pago '{metodo_pago.nombre_metodo_pago}': {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()


def obtener_todos_metodos_pago():
    conexion = obtener_conexion()
    metodos_pago = []
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre_metodo_pago, numero_tarjeta, cvv, titular, predeterminado, 
                       fecha_vencimiento, fecha_creacion, usuario_id
                FROM metodo_pago
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                metodo_pago = claseMetodoPago(*resultado)
                metodos_pago.append(metodo_pago)
        logger.info(f"{len(metodos_pago)} métodos de pago obtenidos.")
        return metodos_pago
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener métodos de pago: {e}")
        return []
    finally:
        if conexion:
            conexion.close()


def obtener_metodo_pago_por_id(id):
    conexion = obtener_conexion()
    metodo_pago = None
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre_metodo_pago, numero_tarjeta, cvv, titular, predeterminado, 
                       fecha_vencimiento, fecha_creacion, usuario_id
                FROM metodo_pago
                WHERE id = %s
            """
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                metodo_pago = claseMetodoPago(*resultado)
                logger.info(f"Método de pago obtenido: {metodo_pago}.")
            else:
                logger.warning(f"No se encontró un método de pago con id {id}.")
        return metodo_pago
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener método de pago con id {id}: {e}")
        return None
    finally:
        if conexion:
            conexion.close()


def actualizar_metodo_pago(metodo_pago):
    if not metodo_pago.nombre_metodo_pago or not metodo_pago.nombre_metodo_pago.strip():
        logger.warning("El nombre del método de pago está vacío o es inválido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                UPDATE metodo_pago
                SET nombre_metodo_pago = %s, numero_tarjeta = %s, cvv = %s, titular = %s, 
                    predeterminado = %s, fecha_vencimiento = %s, usuario_id = %s
                WHERE id = %s
            """
            cursor.execute(sql, (metodo_pago.nombre_metodo_pago, metodo_pago.numero_tarjeta, metodo_pago.cvv,
                                 metodo_pago.titular, metodo_pago.predeterminado, metodo_pago.fecha_vencimiento,
                                 metodo_pago.usuario_id, metodo_pago.id))
        conexion.commit()
        logger.info(f"Método de pago con id {metodo_pago.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar método de pago con id {metodo_pago.id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()


def eliminar_metodo_pago(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql_check = "SELECT COUNT(*) FROM transacciones WHERE metodo_pago_id = %s"
            cursor.execute(sql_check, (id,))
            count = cursor.fetchone()[0]
            if count > 0:
                logger.warning(f"No se puede eliminar el método de pago con id {id}: tiene {count} transacciones asociadas.")
                return False

            sql = "DELETE FROM metodo_pago WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Método de pago con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar método de pago con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()
