from bd import obtener_conexion
from logger_config import logger
from clases import Producto
import mysql.connector

def insertar_producto(producto):
    if not isinstance(producto, Producto):
        logger.warning("Se debe proporcionar un objeto Producto.")
        return None

    if not producto.nombre or not producto.nombre.strip():
        logger.warning("El nombre del producto no puede estar vacío.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO producto (nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.imagen, producto.fecha_registro, producto.estado, producto.categoria_id))
            conexion.commit()

            producto_id = cursor.lastrowid
            cursor.execute("SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id FROM producto WHERE id = %s", (producto_id,))
            result = cursor.fetchone()
            if result:
                return Producto(*result)
            else:
                logger.error(f"Error al obtener el producto después de la inserción. ID: {producto_id}")
                return None

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
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id FROM producto"
            cursor.execute(sql)
            productos = [Producto(*row) for row in cursor.fetchall()]
        logger.info(f"{len(productos)} productos obtenidos.")
        return productos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener productos: {e}")
        return None # Retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

ESTADO_DESTACADOS = 'destacados' # Es mejor definir esto como una constante global

def obtener_productos_destacados():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id
                FROM producto 
                WHERE estado = %s
            """
            cursor.execute(sql, (ESTADO_DESTACADOS,))
            productos = [Producto(*row) for row in cursor.fetchall()]
        logger.info(f"{len(productos)} productos destacados obtenidos.")
        return productos
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener productos destacados: {e}")
        return None # Retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, descripcion, precio, stock, imagen, fecha_registro, estado, categoria_id FROM producto WHERE id = %s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                producto = Producto(*resultado)
                logger.info(f"Producto obtenido: {producto}.")
                return producto
            else:
                logger.warning(f"No se encontró un producto con id {id}.")
                return None # Retorna None si no se encuentra el producto.
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener producto: {e}")
        return None # Retorna None en caso de error
    finally:
        if conexion:
            conexion.close()

def actualizar_producto(producto):
    if not isinstance(producto, Producto):
        logger.warning("Se debe proporcionar un objeto Producto.")
        return False #Puedes dejarlo asi para tu logica
    if not producto.nombre or not producto.nombre.strip():
        logger.warning("El nombre del producto no puede estar vacío.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, stock = %s, imagen = %s, fecha_registro = %s, estado = %s, categoria_id = %s WHERE id = %s"
            cursor.execute(sql, (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.imagen, producto.fecha_registro, producto.estado, producto.categoria_id, producto.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar producto con id {producto.id}: {e}")
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
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar producto con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()