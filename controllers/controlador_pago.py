from bd import obtener_conexion
from clases import clasePago
from logger_config import logger
import mysql.connector

def insertar_pago(pago):
    if not isinstance(pago, clasePago):
        logger.warning("Se debe proporcionar un objeto Pago.")
        return False

    if not pago.estado or not pago.estado.strip() or not pago.metodo_pago or not pago.metodo_pago.strip() or pago.monto is None:
        logger.warning("El estado, método de pago y monto no pueden estar vacíos.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pago (fecha, monto, estado, metodo_pago, pedido_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (pago.fecha, pago.monto, pago.estado, pago.metodo_pago, pago.pedido_id))
        conexion.commit()
        pago.id = cursor.lastrowid
        logger.info(f"Pago insertado exitosamente con ID: {pago.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el pago: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_pagos():
    conexion = obtener_conexion()
    pagos = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha, monto, estado, metodo_pago, pedido_id FROM pago"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                pago = clasePago(*resultado)
                pagos.append(pago)
        logger.info(f"{len(pagos)} pagos obtenidos.")
        return pagos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pagos: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_pago_por_id(id):
    conexion = obtener_conexion()
    pago = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha, monto, estado, metodo_pago, pedido_id FROM pago WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                pago = clasePago(*resultado)
                logger.info(f"Pago obtenido: {pago}.")
        return pago
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pago: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_estado_pago(id, nuevo_estado):
    """Actualiza el estado de un pago.

    Args:
        id: El ID del pago.
        nuevo_estado: El nuevo estado del pago (ej: "completado", "rechazado", "anulado").

    Returns:
        True si la actualización fue exitosa, False en caso contrario.
    """
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE pago SET estado = %s WHERE id = %s"
            cursor.execute(sql, (nuevo_estado, id))
        conexion.commit()
        logger.info(f"Estado del pago con id {id} actualizado a {nuevo_estado}.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar el estado del pago con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()