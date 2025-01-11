import logging

# Configuración básica de logging
logging.basicConfig(
    level=logging.DEBUG,  # Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Archivo donde se almacenan los logs
        logging.StreamHandler()          # Muestra los logs en consola
    ]
)

# Crear un logger personalizado
logger = logging.getLogger("py_monkey3d")
