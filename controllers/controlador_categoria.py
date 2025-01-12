from bd import obtener_conexion
from clases import claseCategoría
from logger_config import logger
import mysql.connector  # Importar el conector específico

def insertar_categoria(nombre):

    if not nombre or not nombre.strip():
        logger.warning("El nombre de la categoría está vacío o es inválido.")
        return False

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO categoria(nombre) VALUES (%s)"
            cursor.execute(sql, (nombre,))
        conexion.commit()
        logger.info(f"Categoría '{nombre}' insertada exitosamente.")
        return True
    except mysql.connector.Error as e:  # Capturar excepción específica
        logger.error(f"Error al insertar la categoría '{nombre}': {e}")
        return False
    finally:
        if conexion: #Verificar si la conexión se creo antes de cerrarla.
            conexion.close()

def obtener_todas_categorias():
    conexion = obtener_conexion()
    categorias = []
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, fecha_creacion FROM categoria"
            cursor.execute(sql)
            categorias = cursor.fetchall()
        logger.info(f"{len(categorias)} categorías obtenidas.")
        return categorias
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener categorias: {e}")
        return [] #Retornar una lista vacia en caso de error
    finally:
         if conexion:
            conexion.close()

def obtener_categoria_por_id(id):

    conexion = obtener_conexion()
    categoria = None
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id, nombre, fecha_creacion FROM categoria WHERE id=%s"
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                categoria = claseCategoría(*resultado) #Crear un objeto de la clase categoria con el resultado de la consulta
                logger.info(f"Categoría obtenida: {categoria}.")
            else:
                logger.warning(f"No se encontró una categoría con id {id}.")
        return categoria
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener categoria: {e}")
        return None
    finally:
         if conexion:
            conexion.close()

def actualizar_categoria(id, nombre):
    if not nombre or not nombre.strip():
        logger.warning("El nombre de la categoría está vacío o es inválido.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE categoria SET nombre=%s WHERE id=%s"
            cursor.execute(sql, (nombre, id))
        conexion.commit()
        logger.info(f"Categoría con id {id} actualizada.")
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar categoria con id:{id}: {e}")
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
            logger.info(f"Categoría con id {id} eliminada.")
            return True

    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar categoria con id {id}: {e}")
        conexion.rollback() #Revertir la transacción en caso de error
        return False
    finally:
        if conexion:
            conexion.close()