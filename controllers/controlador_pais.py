from bd import obtener_conexion
from clases import clasePais
from logger_config import logger
import mysql.connector

def obtener_todos_paises():
    conexion=obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """ 
                select id,nombre,codigo_iso,disponible from pais
                """
            )
        conexion.commit()
        return True   
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener paises.{str(e)}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()
def obtener_todos_pais_por_id(id):
    conexion=obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """ 
                select id,nombre,codigo_iso,disponible from pais
                where id=%s
                """,(id,)
            )
        conexion.commit()
        return True   
    except mysql.connector.Error as e:
        logger.error(f"Error al obtener pais.{str(e)}")
        if conexion:
            conexion.rollback()
        return None
    finally:
        if conexion:
            conexion.close()

def insertar_pais(nombre,codigo_iso):
    conexion=obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
            """
            insert into pais (nombre,codigo_iso) values(%s,%s)
            """,(nombre,codigo_iso)
        )
        conexion.commit()
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al insertar el pais {nombre}: {e}")
        if conexion:
            conexion.rollback()
        return False    
    finally:
        if conexion:
            conexion.close()

def dar_de_baja_pais(id):
    conexion=obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
            """
            update pais set disponibilidad=0 
            where id=%s
            """,(id,)
            )
        conexion.commit()
        return True
    except mysql.connector.Error as e:
        logger.error(f"No se pudo dar de baja al pais: {e}")
        if conexion:
            conexion.rollback()
        return False   
    finally:
        if conexion:
            conexion.close()   
def eliminar_pais(id):
    conexion=obtener_conexion()
    try:   
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                delete from pais where id=%s
                """,(id,)
            )
        conexion.commit()
        return True
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar pais. {e}")
        if conexion:
            conexion.rollback()
        return False    
    finally:
        if conexion:
            conexion.close()
