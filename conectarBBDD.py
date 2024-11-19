from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

clienteMDB= MongoClient('mongodb+srv://'+usuario+':'+password+'@mongo.ctgjd.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)

baseDatos = clienteMDB['AlbertoCaroBarrera']

coleccion = baseDatos["Miprimeracoleccion"]

documento = {'nombre' : 'Alberto',
             'apellido' : 'Caro'
}

insercion = coleccion.insert_one(documento)