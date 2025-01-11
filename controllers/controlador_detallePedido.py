from bd import obtener_conexion
from logger_config import logger
from clases import claseDetallePedido
import mysql.connector


def insertar_detalle_pedido(detalle_pedido):
    if not isinstance(detalle_pedido, claseDetallePedido):
        logger.warning("Se debe proporcionar un objeto Detalle_pedido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO detalle_pedido (precioUnitario, cantidad, fecha_creacion, producto_id, pedido_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (detalle_pedido.precioUnitario, detalle_pedido.cantidad, detalle_pedido.fecha_creacion, detalle_pedido.producto_id, detalle_pedido.pedido_id))
        conexion.commit()
        detalle_pedido.id = cursor.lastrowid
        logger.info(f"Detalle de pedido insertado exitosamente con ID: {detalle_pedido.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el detalle de pedido: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_detalles_pedido():
    conexion = obtener_conexion()
    detalles_pedido = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, precioUnitario, cantidad, fecha_creacion, producto_id, pedido_id FROM detalle_pedido"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                detalle_pedido = claseDetallePedido(*resultado)
                detalles_pedido.append(detalle_pedido)
        logger.info(f"{len(detalles_pedido)} detalles de pedido obtenidos.")
        return detalles_pedido
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener detalles de pedido: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_detalle_pedido_por_id(id):
    conexion = obtener_conexion()
    detalle_pedido = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, precioUnitario, cantidad, fecha_creacion, producto_id, pedido_id FROM detalle_pedido WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                detalle_pedido = claseDetallePedido(*resultado)
                logger.info(f"Detalle de pedido obtenido: {detalle_pedido}.")
        return detalle_pedido
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener detalle de pedido: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_detalle_pedido(detalle_pedido):
    if not isinstance(detalle_pedido, claseDetallePedido):
        logger.warning("Se debe proporcionar un objeto Detalle_pedido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE detalle_pedido SET precioUnitario = %s, cantidad = %s, fecha_creacion = %s, producto_id = %s, pedido_id = %s WHERE id = %s"
            cursor.execute(sql, (detalle_pedido.precioUnitario, detalle_pedido.cantidad, detalle_pedido.fecha_creacion, detalle_pedido.producto_id, detalle_pedido.pedido_id, detalle_pedido.id))
        conexion.commit()
        logger.info(f"Detalle de pedido con id {detalle_pedido.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar detalle de pedido con id {detalle_pedido.id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_detalle_pedido(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM detalle_pedido WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Detalle de pedido con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar detalle de pedido con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()
