from bd import obtener_conexion
from logger_config import logger
from clases import claseProducto
import mysql.connector

def insertar_producto(producto):
    if not isinstance(producto, claseProducto):
        logger.warning("Se debe proporcionar un objeto Producto.")
        return False

    if not producto.nombre or not producto.nombre.strip():
        logger.warning("El nombre del producto no puede estar vacío.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO producto (nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.imagen, producto.fecha_registro, producto.estado, producto.categoria_id))
        conexion.commit()
        producto.id = cursor.lastrowid
        logger.info(f"Producto '{producto.nombre}' insertado exitosamente con ID: {producto.id}")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el producto: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def obtener_todos_productos():
    conexion = obtener_conexion()
    productos = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id FROM producto"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                producto = claseProducto(*resultado)
                productos.append(producto)
        logger.info(f"{len(productos)} productos obtenidos.")
        return productos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener productos: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    producto = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id FROM producto WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                producto = claseProducto(*resultado)
                logger.info(f"Producto obtenido: {producto}.")
        return producto
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener producto: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_producto(producto):
    if not isinstance(producto, claseProducto):
        logger.warning("Se debe proporcionar un objeto Producto.")
        return False
    if not producto.nombre or not producto.nombre.strip():
        logger.warning("El nombre del producto no puede estar vacío.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, stock = %s, imagen = %s, fecha_registro = %s, estado = %s, categoria_id = %s WHERE id = %s"
            cursor.execute(sql, (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.imagen, producto.fecha_registro, producto.estado, producto.categoria_id, producto.id))
        conexion.commit()
        logger.info(f"Producto con id {producto.id} actualizado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar producto con id {producto.id}: {e}")
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
        logger.info(f"Producto con id {id} eliminado.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar producto con id {id}: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()