from bd import obtener_conexion
from logger_config import logger
from clases import  claseProducto as Producto
import mysql.connector

def insertar_producto(nombre, descripcion, precio, stock, imagen, estado, categoria_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO producto (nombre, descripcion, precio, stock, imagen, estado, categoria_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, descripcion, precio, stock, imagen, estado, categoria_id))
            conexion.commit()
        logger.info(f"Producto {nombre} registrado")
        return True

    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el producto: {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_productos():
    conexion = obtener_conexion()
    productos=[]
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, descripcion, precio, stock, imagen, estado, categoria_id FROM producto order by 1"
            cursor.execute(sql)
            productos=cursor.fetchall()
        logger.info(f"{len(productos)} productos obtenidos.")
        return productos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener productos: {e}")
        return None 
    finally:
        if conexion:
            conexion.close()

def obtener_productos_destacados():
    conexion = obtener_conexion()
    productos=[]
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id
                FROM producto 
                WHERE estado = 'destacados'
            """
            cursor.execute(sql)
            productos = cursor.fetchall()
        logger.info(f"{len(productos)} productos destacados obtenidos.")
        return productos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener productos destacados: {e}")
        return None 
    finally:
        if conexion:
            conexion.close()

def obtener_productos_nuevos():
    conexion = obtener_conexion()
    productos_nuevos=[]
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id
                FROM producto 
                WHERE estado = 'nuevos'
            """
            cursor.execute(sql)
            productos_nuevos=cursor.fetchall()
        logger.info(f"{len(productos_nuevos)} productos nuevos obtenidos.")
        return productos_nuevos 
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener productos nuevos: {e}")
        return None 
    finally:
        if conexion:
            conexion.close()

def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id FROM producto WHERE id = %s"
            cursor.execute(sql, (id,))
            producto = cursor.fetchone()
        logger.info(f"Producto con id : {id} obtenido")   
        return producto
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener producto: {e}")
        return None 
    finally:
        if conexion:
            conexion.close()

def actualizar_producto(nombre, descripcion, precio, stock, imagen, estado, categoria_id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, stock = %s, imagen = %s, estado = %s, categoria_id = %s WHERE id = %s"
            cursor.execute(sql, (nombre, descripcion, precio, stock, imagen, estado, categoria_id))
            conexion.commit()
            return True    
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar producto con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_producto(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM producto WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
        logger.info(f"Producto con id : {id} eliminado con éxito")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar producto con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()