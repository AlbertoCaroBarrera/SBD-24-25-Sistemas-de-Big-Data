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

def obtener_registros_condicion_u_otra(db, filtros):
    """Obtiene registros que cumplan al menos una de las condiciones proporcionadas."""
    coleccion = db['Pacientes']
    
    # Usamos el operador $or para combinar las condiciones
    filtro_or = {"$or": filtros}
    
    registros = coleccion.find(filtro_or)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_registros_no_cumple_condicion(db, atributo, valor):
    """Obtiene registros que no cumplen con una condición específica."""
    coleccion = db['Pacientes']
    
    # Usamos el operador $ne para obtener documentos donde el atributo no es igual al valor
    filtro = {atributo: {"$ne": valor}}
    
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)


def eliminar_registro(db, filtro):
    """Eliminar un registro de la colección 'Pacientes' basado en un filtro."""
    coleccion = db['Pacientes']
    
    # Usamos delete_one para eliminar un único documento que coincida con el filtro
    resultado = coleccion.delete_one(filtro)
    
    # Retornamos el número de documentos eliminados (debería ser 1 si se elimina correctamente)
    return resultado.deleted_count

def eliminar_varios_registros(db, filtro):
    """Eliminar varios registros de la colección 'Pacientes' basado en un filtro."""
    coleccion = db['Pacientes']
    
    # Usamos delete_many para eliminar todos los documentos que coincidan con el filtro
    resultado = coleccion.delete_many(filtro)
    
    # Retornamos el número de documentos eliminados
    return resultado.deleted_count

def obtener_registros_ordenados(db, atributo):
    """Obtener todos los registros de la colección 'Pacientes' ordenados de forma ascendente por un atributo."""
    coleccion = db['Pacientes']
    
    # Usamos find() para obtener todos los registros y sort() para ordenarlos
    registros = coleccion.find().sort(atributo, 1)  # 1 es para orden ascendente, -1 sería descendente
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)


def obtener_registros_ordenados_descendente(db, atributo):
    """Obtener todos los registros de la colección 'Pacientes' ordenados de forma descendente por un atributo."""
    coleccion = db['Pacientes']
    
    # Usamos find() para obtener todos los registros y sort() para ordenarlos de manera descendente
    registros = coleccion.find().sort(atributo, -1)  # -1 es para orden descendente, 1 sería ascendente
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_primeros_10_registros(db):
    """Obtener los primeros 10 registros de la colección 'Pacientes'."""
    coleccion = db['Pacientes']
    
    # Usamos find() para obtener los registros y limit(10) para limitar el número de registros a 10
    registros = coleccion.find().limit(10)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)


def obtener_registros_por_regex(db, campo, patron):
    """Obtener registros filtrados por una expresión regular."""
    coleccion = db['Pacientes']
    
    # Usamos el operador $regex para realizar la búsqueda con el patrón proporcionado
    filtro = {campo: {"$regex": patron, "$options": "i"}}  # $options: "i" es para búsqueda insensible a mayúsculas/minúsculas
    
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)

def obtener_enfermedades_por_sintomas(db, lista_sintomas):
    """Obtiene todas las enfermedades que contengan al menos uno de los síntomas especificados."""
    coleccion = db['Enfermedades']
    
    # Usamos el operador $in para filtrar por los síntomas presentes en el array
    filtro = {"sintomas": {"$in": lista_sintomas}}  # Filtra por síntomas en la lista proporcionada
    
    # Ejecutamos la consulta
    registros = coleccion.find(filtro)
    
    # Convertimos los registros a una lista y los devolvemos
    return list(registros)




# Coleccion extra de enfermedades para hacer ejercicio de arrays
def insertar_enfermedad(db, nombre, descripcion, sintomas, tratamiento=None):
    """Insertar una nueva enfermedad en la colección 'Enfermedades'."""
    coleccion = db["Enfermedades"]
    
    # Creamos el documento de la enfermedad
    enfermedad = {
        "nombre": nombre,
        "descripcion": descripcion,
        "sintomas": sintomas,  # síntomas debe ser una lista (array)
        "tratamiento": tratamiento
    }
    
    # Insertamos el documento en la colección
    resultado = coleccion.insert_one(enfermedad)
    
    # Retornamos el ID del documento insertado
    return resultado.inserted_id
