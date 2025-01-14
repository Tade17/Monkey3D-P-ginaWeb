from bd import obtener_conexion
from logger_config import logger
from clases import Detalle_pedido  # Importa la clase correcta
import mysql.connector

def insertar_detalle_pedido(detalle_pedido):
    if not isinstance(detalle_pedido, Detalle_pedido):
        logger.warning("Se debe proporcionar un objeto Detalle_pedido.")
        return None  # Retorna None en lugar de False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO detalle_pedido (precioUnitario, cantidad, fecha_creacion, producto_id, pedido_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (detalle_pedido.precioUnitario, detalle_pedido.cantidad, detalle_pedido.fecha_creacion, detalle_pedido.producto_id, detalle_pedido.pedido_id))
            conexion.commit()

            # Obtener el detalle de pedido recién insertado
            detalle_pedido_id = cursor.lastrowid
            cursor.execute("SELECT id, precioUnitario, cantidad, fecha_creacion, producto_id, pedido_id FROM detalle_pedido WHERE id = %s", (detalle_pedido_id,))
            result = cursor.fetchone()
            if result:
                return Detalle_pedido(*result)
            else:
                logger.error(f"Error al obtener el detalle de pedido después de la inserción. ID: {detalle_pedido_id}")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el detalle de pedido: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_detalles_pedido():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, precioUnitario, cantidad, fecha_creacion, producto_id, pedido_id FROM detalle_pedido"
            cursor.execute(sql)
            detalles_pedido = [Detalle_pedido(*row) for row in cursor.fetchall()]
        logger.info(f"{len(detalles_pedido)} detalles de pedido obtenidos.")
        return detalles_pedido
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener detalles de pedido: {e}")
        return None  # Retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def obtener_detalle_pedido_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, precioUnitario, cantidad, fecha_creacion, producto_id, pedido_id FROM detalle_pedido WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                detalle_pedido = Detalle_pedido(*resultado)
                logger.info(f"Detalle de pedido obtenido: {detalle_pedido}.")
                return detalle_pedido
            else:
                logger.warning(f"No se encontró un detalle de pedido con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener detalle de pedido: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_detalle_pedido(detalle_pedido):
    if not isinstance(detalle_pedido, Detalle_pedido):
        logger.warning("Se debe proporcionar un objeto Detalle_pedido.")
        return False #Puedes dejarlo asi para tu logica si lo necesitas
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE detalle_pedido SET precioUnitario = %s, cantidad = %s, fecha_creacion = %s, producto_id = %s, pedido_id = %s WHERE id = %s"
            cursor.execute(sql, (detalle_pedido.precioUnitario, detalle_pedido.cantidad, detalle_pedido.fecha_creacion, detalle_pedido.producto_id, detalle_pedido.pedido_id, detalle_pedido.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar detalle de pedido con id {detalle_pedido.id}: {e}")
        if conexion:
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar detalle de pedido con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()