from bd import obtener_conexion
from clases import MetodoPago
from logger_config import logger
import mysql.connector

def insertar_metodo_pago(metodo_pago):
    if not isinstance(metodo_pago, MetodoPago):
        logger.warning("Se debe proporcionar un objeto MetodoPago.")
        return None

    if not metodo_pago.nombre_metodo_pago or not metodo_pago.nombre_metodo_pago.strip():
        logger.warning("El nombre del método de pago está vacío o es inválido.")
        return None

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO metodo_pago (nombre_metodo_pago, numero_tarjeta, cvv, titular, predeterminado, 
                                        fecha_vencimiento, usuario_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (metodo_pago.nombre_metodo_pago, metodo_pago.numero_tarjeta, metodo_pago.cvv,
                                metodo_pago.titular, metodo_pago.predeterminado, metodo_pago.fecha_vencimiento,
                                metodo_pago.usuario_id))
            conexion.commit()

            metodo_pago_id = cursor.lastrowid
            cursor.execute("""
                SELECT id, nombre_metodo_pago, numero_tarjeta, cvv, titular, predeterminado, 
                       fecha_vencimiento, fecha_creacion, usuario_id
                FROM metodo_pago
                WHERE id = %s
            """, (metodo_pago_id,))
            result = cursor.fetchone()
            if result:
                return MetodoPago(*result)
            else:
                logger.error(f"Error al obtener el método de pago después de la inserción. ID: {metodo_pago_id}")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el método de pago '{metodo_pago.nombre_metodo_pago}': {e}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def obtener_todos_metodos_pago():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre_metodo_pago, numero_tarjeta, cvv, titular, predeterminado, 
                       fecha_vencimiento, fecha_creacion, usuario_id
                FROM metodo_pago
            """
            cursor.execute(sql)
            metodos_pago = [MetodoPago(*row) for row in cursor.fetchall()]
        logger.info(f"{len(metodos_pago)} métodos de pago obtenidos.")
        return metodos_pago
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener métodos de pago: {e}")
        return None #Retornar None en caso de error
    finally:
        if conexion:
            conexion.close()

def obtener_metodo_pago_por_id(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre_metodo_pago, numero_tarjeta, cvv, titular, predeterminado, 
                       fecha_vencimiento, fecha_creacion, usuario_id
                FROM metodo_pago
                WHERE id = %s
            """
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            if resultado:
                metodo_pago = MetodoPago(*resultado)
                logger.info(f"Método de pago obtenido: {metodo_pago}.")
                return metodo_pago
            else:
                logger.warning(f"No se encontró un método de pago con id {id}.")
                return None
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener método de pago con id {id}: {e}")
        return None #Retornar None en caso de error
    finally:
        if conexion:
            conexion.close()

def actualizar_metodo_pago(metodo_pago):
    if not isinstance(metodo_pago, MetodoPago):
        logger.warning("Se debe proporcionar un objeto MetodoPago.")
        return False #Puedes dejarlo asi para tu logica si lo necesitas
    if not metodo_pago.nombre_metodo_pago or not metodo_pago.nombre_metodo_pago.strip():
        logger.warning("El nombre del método de pago está vacío o es inválido.")
        return False
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = """
                UPDATE metodo_pago
                SET nombre_metodo_pago = %s, numero_tarjeta = %s, cvv = %s, titular = %s, 
                    predeterminado = %s, fecha_vencimiento = %s, usuario_id = %s
                WHERE id = %s
            """
            cursor.execute(sql, (metodo_pago.nombre_metodo_pago, metodo_pago.numero_tarjeta, metodo_pago.cvv,
                                metodo_pago.titular, metodo_pago.predeterminado, metodo_pago.fecha_vencimiento,
                                metodo_pago.usuario_id, metodo_pago.id))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se actualizo al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar método de pago con id {metodo_pago.id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_metodo_pago(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql_check = "SELECT COUNT(*) FROM transacciones WHERE metodo_pago_id = %s"
            cursor.execute(sql_check, (id,))
            count = cursor.fetchone()[0]
            if count > 0:
                logger.warning(f"No se puede eliminar el método de pago con id {id}: tiene {count} transacciones asociadas.")
                return False

            sql = "DELETE FROM metodo_pago WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
            return cursor.rowcount > 0 #retorna true si se elimino al menos una fila
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar método de pago con id {id}: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()