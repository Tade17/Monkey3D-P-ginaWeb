from bd import obtener_conexion
from logger_config import logger
from clases import Pago
import mysql.connector

def insertar_pago(pago):
    if not isinstance(pago, Pago):
        logger.warning("Se debe proporcionar un objeto Pago.")
        return None

    if not pago.estado or not pago.estado.strip() or not pago.metodo_pago or not pago.metodo_pago.strip() or pago.monto is None:
        logger.warning("El estado, método de pago y monto no pueden estar vacíos.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pago (fecha, monto, estado, metodo_pago, pedido_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (pago.fecha, pago.monto, pago.estado, pago.metodo_pago, pago.pedido_id))
            conexion.commit()

            pago_id = cursor.lastrowid
            cursor.execute("SELECT id, fecha, monto, estado, metodo_pago, pedido_id FROM pago WHERE id = %s", (pago_id,))
            result = cursor.fetchone()
            if result:
                return Pago(*result)
            else:
                logger.error(f"Error al obtener el pago después de la inserción. ID: {pago_id}")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el pago: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_pagos():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha, monto, estado, metodo_pago, pedido_id FROM pago"
            cursor.execute(sql)
            pagos = [Pago(*row) for row in cursor.fetchall()]
        logger.info(f"{len(pagos)} pagos obtenidos.")
        return pagos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pagos: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_pago_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha, monto, estado, metodo_pago, pedido_id FROM pago WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                pago = Pago(*resultado)
                logger.info(f"Pago obtenido: {pago}.")
                return pago
            else:
                logger.warning(f"No se encontró un pago con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pago: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_estado_pago(id, nuevo_estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE pago SET estado = %s WHERE id = %s"
            cursor.execute(sql, (nuevo_estado, id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar el estado del pago con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()