from bd import obtener_conexion
from clases import Categoria
from logger_config import logger
import mysql.connector

def insertar_categoria(nombre):
    if not nombre or not nombre.strip():
        logger.warning("El nombre de la categoría está vacío o es inválido.")
        return None  # Retornar None en lugar de False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO categoria(nombre) VALUES (%s)"
            cursor.execute(sql, (nombre,))
            conexion.commit()
            categoria_id = cursor.lastrowid #obtengo el id insertado
            cursor.execute("SELECT id, nombre, fecha_creacion FROM categoria WHERE id = %s", (categoria_id,))
            result = cursor.fetchone()
            if result:
                return Categoria(*result) #retorno el objeto categoria creado
            else:
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar la categoría '{nombre}': {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todas_categorias():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, fecha_creacion FROM categoria"
            cursor.execute(sql)
            categorias = [Categoria(*row) for row in cursor.fetchall()] #lista de objetos categoria
        logger.info(f"{len(categorias)} categorías obtenidas.")
        return categorias
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener categorias: {e}")
        return None  # Retornar None en caso de error
    finally:
        if conexion:
            conexion.close()

def obtener_categoria_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, fecha_creacion FROM categoria WHERE id=%s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                categoria = Categoria(*resultado)
                logger.info(f"Categoría obtenida: {categoria}.")
                return categoria
            else:
                logger.warning(f"No se encontró una categoría con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener categoria: {e}")
        return None
    finally:
        if conexion:
            conexion.close()

def actualizar_categoria(id, nombre):
    if not nombre or not nombre.strip():
        logger.warning("El nombre de la categoría está vacío o es inválido.")
        return False #puedes dejarlo asi si lo necesitas para tu logica
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE categoria SET nombre=%s WHERE id=%s"
            cursor.execute(sql, (nombre, id))
            conexion.commit()
            return cursor.rowcount > 0  #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar categoria con id:{id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_categoria(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Verificamos si hay productos asociados a la categoría
            sql_check = "SELECT COUNT(*) FROM producto WHERE categoria_id = %s"
            cursor.execute(sql_check, (id,))
            count = cursor.fetchone()[0]

            if count > 0:
                logger.warning(f"No se puede eliminar la categoría con id {id}: tiene {count} producto(s) asociado(s).")
                return False  # No se elimina si hay productos asociados

            # Si no hay productos asociados, procedemos con la eliminación
            sql_delete = "DELETE FROM categoria WHERE id = %s"
            cursor.execute(sql_delete, (id,))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila

    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar categoria con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()