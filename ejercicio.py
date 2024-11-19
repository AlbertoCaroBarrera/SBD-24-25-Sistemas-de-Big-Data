from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()
libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]


miquery = {"paginas":1072}
libros = librosColeccion.find(miquery)
for l in libros:
    print(f"Que tenga 1072 paginas {l}")
    

print("Listado de libros con precio mayor o igual a 5 y el titulo empiece por 1")
libros= librosColeccion.find({ "$and" : [
                                                     { "titulo" : {"$regex": "^1"}},
                                                     { "precio" : { "$gte":5} }
                                                   ]
                                           }
                                           )
for l in libros:
    print(f"Libros que cumple: {l}")
    
    
print("Que no tenga más de 600 paginas y cuestan más de 30 euros")
libros= librosColeccion.find({ "$nor" : [
                                                     { "precio" : { "$gt":30}},
                                                     { "paginas" : { "$gt":600} }
                                                   ]
                                           }
                                           ).sort("titulo",-1)
for l in libros:
    print(f"Libros que cumple: {l}")