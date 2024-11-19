# config.py
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de MongoDB
USUARIO_MONGODB = os.getenv("USUARIO_MONGODB")
PASSWORD_MONGODB = os.getenv("PASSWORD_MONGODB")
CLUSTER_MONGODB = os.getenv("CLUSTER_MONGODB")
