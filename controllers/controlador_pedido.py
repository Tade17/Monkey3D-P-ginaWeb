from bd import obtener_conexion
from logger_config import logger
from clases import clasePedido
import mysql.connector


def insertar_pedido(pedido):
    if not isinstance(pedido, clasePedido):
        logger.warning("Se debe proporcionar un objeto Pedido.")
        return False

    if not pedido.estado or not pedido.estado.strip():
        logger.warning("El estado del pedido no puede estar vacío.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pedido (fecha_pedido, total, estado, domicilio_id, usuario_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (pedido.fecha_pedido, pedido.total, pedido.estado, pedido.domicilio_id, pedido.usuario_id))
        conexion.commit()
        pedido.id = cursor.lastrowid
        logger.info(f"Pedido insertado exitosamente con ID: {pedido.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el pedido: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_pedidos():
    conexion = obtener_conexion()
    pedidos = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha_pedido, total, estado, domicilio_id, usuario_id FROM pedido"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                pedido = clasePedido(*resultado)
                pedidos.append(pedido)
        logger.info(f"{len(pedidos)} pedidos obtenidos.")
        return pedidos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pedidos: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_pedido_por_id(id):
    conexion = obtener_conexion()
    pedido = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha_pedido, total, estado, domicilio_id, usuario_id FROM pedido WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                pedido = clasePedido(*resultado)
                logger.info(f"Pedido obtenido: {pedido}.")
        return pedido
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pedido: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_pedido(pedido):
    if not isinstance(pedido, clasePedido):
        logger.warning("Se debe proporcionar un objeto Pedido.")
        return False
    if not pedido.estado or not pedido.estado.strip():
        logger.warning("El estado del pedido no puede estar vacío.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE pedido SET fecha_pedido = %s, total = %s, estado = %s, domicilio_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (pedido.fecha_pedido, pedido.total, pedido.estado, pedido.domicilio_id, pedido.usuario_id, pedido.id))
        conexion.commit()
        logger.info(f"Pedido con id {pedido.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar pedido con id {pedido.id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_pedido(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM pedido WHERE id = %s"
            cursor.execute(sql, (id,))
        conexion.commit()
        logger.info(f"Pedido con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar pedido con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()