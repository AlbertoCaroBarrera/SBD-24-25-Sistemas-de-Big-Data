from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()
libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

miquery = { "titulo": "1984" }
nuevosValores = { "$set": { "titulo": "Reina Roja" } }

print("Libros actualizados")
resultado = librosColeccion.update_many(miquery, nuevosValores)
