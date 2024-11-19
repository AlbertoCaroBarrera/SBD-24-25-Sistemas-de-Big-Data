# db.py
from pymongo import MongoClient
from config import USUARIO_MONGODB, PASSWORD_MONGODB, CLUSTER_MONGODB

def conectar_db():
    """Conectar a MongoDB utilizando las credenciales del archivo .env."""
    try:
        # Formamos la URL de conexión con las credenciales
        uri = f'mongodb+srv://{USUARIO_MONGODB}:{PASSWORD_MONGODB}@{CLUSTER_MONGODB}.ctgjd.mongodb.net/?retryWrites=true&w=majority&appName={CLUSTER_MONGODB}'
        
        # Conectamos al cliente de MongoDB
        cliente = MongoClient(uri)
        
        # Verificamos que la conexión fue exitosa
        print("Conexión exitosa a MongoDB")
        
        # Retornamos el cliente para acceder a las bases de datos
        return cliente
    except Exception as e:
        print(f"Error al conectar con MongoDB: {e}")
        return None

def insertar_paciente(db, nombre, edad, email, direccion, telefono):
    """Insertar un registro en la bbdd 'salud'."""
    coleccion = db["Pacientes"]
    
    # Creamos el documento con los datos proporcionados
    registro = {
        "nombre": nombre,
        "edad": int(edad),
        "email": email,
        "direccion": direccion,
        "telefono": telefono
    }
    
    # Insertamos el documento en la colección y obtenemos el ID del documento insertado
    resultado = coleccion.insert_one(registro)
    
    # Retornamos el ID del documento insertado
    return resultado.inserted_id


def insertar_varios_pacientes(db, registros):
    """Insertar varios registros en la bbdd 'salud'."""
    
    coleccion = db["Pacientes"]
    
    # Insertar varios documentos de una vez utilizando insert_many
    resultado = coleccion.insert_many(registros)
    
    # Retorna los IDs de los documentos insertados
    return resultado.inserted_ids

def actualizar_paciente(db, filtro, nuevos_datos):
    """
    Actualizar un registro en la colección 'salud'.
    
    :param db: la base de datos
    :param filtro: el filtro para encontrar el registro a actualizar (ej. {'nombre': 'Ana'})
    :param nuevos_datos: los datos a actualizar (ej. {'edad': 26})
    :return: el número de documentos modificados
    """
    coleccion = db["Pacientes"]
    
    # Usamos update_one para actualizar un solo registro
    resultado = coleccion.update_one(filtro, {"$set": nuevos_datos})
    
    # Retornamos el número de documentos modificados
    return resultado.modified_count

def actualizar_varios_pacientes(db, filtro, nuevos_datos):
    """Actualizar varios pacientes en la colección 'Pacientes'."""
    coleccion = db['Pacientes']
    resultado = coleccion.update_many(filtro, {"$set": nuevos_datos})
    return resultado.modified_count

def obtener_varios_registros(db, filtro):
    """Obtiene varios registros de la colección 'Pacientes' basados en un filtro."""
    coleccion = db['Pacientes']
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_varios_registros_por_filtro_multiple(db, filtro):
    """Obtiene varios registros de la colección 'Pacientes' basados en un filtro con varios atributos."""
    coleccion = db['Pacientes']  # Nombre de la colección
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_registros_no_nulos(db, atributo):
    """Obtiene todos los registros donde el atributo no tenga valor nulo o no esté ausente."""
    coleccion = db['Pacientes']  # Nombre de la colección
    filtro = {atributo: {"$ne": None}}  # Filtro para excluir valores nulos (None)
    
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_registros_sin_atributo(db, atributo):
    """Obtiene todos los registros donde el atributo no exista."""
    coleccion = db['Pacientes']  # Nombre de la colección
    filtro = {atributo: {"$exists": False}}  # Filtro para encontrar documentos sin el atributo
    
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_registros_por_lista_de_valores(db, atributo, lista_valores):
    """Obtiene todos los registros donde el valor del atributo esté en la lista de valores proporcionada."""
    coleccion = db['Pacientes']  # Nombre de la colección
    filtro = {atributo: {"$in": lista_valores}}  # Filtro con el operador $in
    
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_registros_mayores(db, atributo, valor):
    """Obtiene todos los registros donde el valor del atributo numérico sea mayor que el valor especificado."""
    coleccion = db['Pacientes']  # Nombre de la colección
    filtro = {atributo: {"$gt": valor}}  # Filtro con el operador $gt
    
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)