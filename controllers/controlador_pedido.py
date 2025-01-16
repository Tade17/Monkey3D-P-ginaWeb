from bd import obtener_conexion
from logger_config import logger
from clases import clasePedido as Pedido
import mysql.connector

def insertar_pedido(total,domicilio_id,usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pedido (total,domicilio_id, usuario_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (total,domicilio_id,usuario_id))
            conexion.commit()
        return True
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
    pedidos=[]
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, fecha_pedido, total, estado, domicilio_id, usuario_id FROM pedido"
            cursor.execute(sql)
            pedidos=cursor.fetchall()
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
            pedido = cursor.fetchone()
        return pedido   
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pedido: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_pedido(total,domicilio_id,usuario_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE pedido SET fecha_pedido = %s, total = %s, estado = %s, domicilio_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (total,domicilio_id,usuario_id))
            conexion.commit()
        logger.info(f"Pedido actualizado con éxito")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar pedido con id {id}: {e}")
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
        logger.info(f"pedido con id: {id} eliminado con éxito")    
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar pedido con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()