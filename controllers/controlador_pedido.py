from bd import obtener_conexion
from logger_config import logger
from clases import Pedido
import mysql.connector

def insertar_pedido(pedido):
    if not isinstance(pedido, Pedido):
        logger.warning("Se debe proporcionar un objeto Pedido.")
        return None

    if not pedido.estado or not pedido.estado.strip():
        logger.warning("El estado del pedido no puede estar vacío.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pedido (fecha_pedido, total, estado, domicilio_id, usuario_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (pedido.fecha_pedido, pedido.total, pedido.estado, pedido.domicilio_id, pedido.usuario_id))
            conexion.commit()

            pedido_id = cursor.lastrowid
            cursor.execute("SELECT id, fecha_pedido, total, estado, domicilio_id, usuario_id FROM pedido WHERE id = %s", (pedido_id,))
            result = cursor.fetchone()
            if result:
                return Pedido(*result)
            else:
                logger.error(f"Error al obtener el pedido después de la inserción. ID: {pedido_id}")
                return None

    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el pedido: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_pedidos():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha_pedido, total, estado, domicilio_id, usuario_id FROM pedido"
            cursor.execute(sql)
            pedidos = [Pedido(*row) for row in cursor.fetchall()]
        logger.info(f"{len(pedidos)} pedidos obtenidos.")
        return pedidos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pedidos: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_pedido_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha_pedido, total, estado, domicilio_id, usuario_id FROM pedido WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                pedido = Pedido(*resultado)
                logger.info(f"Pedido obtenido: {pedido}.")
                return pedido
            else:
                logger.warning(f"No se encontró un pedido con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pedido: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_pedido(pedido):
    if not isinstance(pedido, Pedido):
        logger.warning("Se debe proporcionar un objeto Pedido.")
        return False #Puedes dejarlo asi para tu logica
    if not pedido.estado or not pedido.estado.strip():
        logger.warning("El estado del pedido no puede estar vacío.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE pedido SET fecha_pedido = %s, total = %s, estado = %s, domicilio_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (pedido.fecha_pedido, pedido.total, pedido.estado, pedido.domicilio_id, pedido.usuario_id, pedido.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar pedido con id {pedido.id}: {e}")
        if conexion:
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar pedido con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()