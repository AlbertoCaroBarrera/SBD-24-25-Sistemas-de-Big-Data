# menu.py
from db import * 

def mostrar_menu():
    # Conectar a la base de datos
    cliente = conectar_db()
    if cliente is None:
        print("No se pudo conectar a la base de datos.")
        return

    # Seleccionar la base de datos (puedes cambiar 'mi_base_de_datos' por tu base de datos real)
    db = cliente['Salud']  

    while True:
        # Mostrar las opciones del menú
        print("1. Insertar un nuevo paciente")
        print("2. Insertar varios pacientes")
        print("3. Actualizar un paciente")
        print("4. Actualizar varios pacientes por nombre")
        print("5. Obtener varios pacientes por filtro")
        print("6. Obtener varios pacientes por filtro con varios atributos")
        print("7. Obtener pacientes sin valores nulos en un atributo")
        print("8. Obtener pacientes sin un atributo específico")
        print("9. Obtener pacientes por lista de valores en un atributo")
        print("10. Obtener pacientes con un atributo numérico mayor que el valor especificado")
        print("11. Obtener pacientes con condición 'u otra' (operador OR)")
        print("12. Obtener pacientes que no cumplan una condición específica")
        print("13. Eliminar un registro de la colección")
        print("14. Eliminar varios registros de la colección")
        print("15. Realiza una búsqueda y ordénala de forma ascendente")
        print("16. Realiza una búsqueda y ordénala de forma descendente")
        print("17. Realiza una búsqueda limitada a 10 registros")
        print("18. Realizar una búsqueda por expresión regular")
        print("19. Obtener enfermedades con sintomas indicados")
        print("21. Insertar una nueva enfermedad")
        print("22. Salir")
        print()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Pedir los datos al usuario
            nombre = input("Nombre del paciente: ")
            edad = input("Edad del paciente: ")
            email = input("Email del paciente: ")
            direccion = input("Dirección del paciente: ")
            telefono = input("Teléfono del paciente: ")
            
            # Insertar el paciente en la base de datos
            inserted_id = insertar_paciente(db, nombre, edad, email, direccion, telefono)
            print(f"Paciente insertado con ID: {inserted_id}")
        
        elif opcion == '2':
            # Insertar varios pacientes
            try:
                num_pacientes = int(input("¿Cuántos pacientes deseas insertar? "))
                pacientes = []
                for _ in range(num_pacientes):
                    nombre = input("Nombre del paciente: ")
                    edad = input("Edad del paciente: ")
                    email = input("Email del paciente: ")
                    direccion = input("Dirección del paciente: ")
                    telefono = input("Teléfono del paciente: ")
                    
                    # Crear un paciente como diccionario y añadirlo a la lista
                    pacientes.append({
                        "nombre": nombre,
                        "edad": edad,
                        "email": email,
                        "direccion": direccion,
                        "telefono": telefono
                    })
                
                # Insertar varios pacientes
                inserted_ids = insertar_varios_pacientes(db, pacientes)
                print(f"Pacientes insertados con los IDs: {inserted_ids}")
            except ValueError:
                print("Por favor, ingresa un número válido para la cantidad de pacientes.")
        
        elif opcion == '3':
            # Actualizar un paciente
            nombre_filtro = input("Ingrese el nombre del paciente que desea actualizar: ")
            nuevo_nombre = input("Nuevo nombre del paciente (deje en blanco si no se va a cambiar): ")
            nueva_edad = input("Nueva edad del paciente (deje en blanco si no se va a cambiar): ")
            nuevo_email = input("Nuevo email del paciente (deje en blanco si no se va a cambiar): ")
            nueva_direccion = input("Nueva dirección del paciente (deje en blanco si no se va a cambiar): ")
            nuevo_telefono = input("Nuevo teléfono del paciente (deje en blanco si no se va a cambiar): ")
            
            # Crear el filtro y los nuevos datos a actualizar
            filtro = {"nombre": nombre_filtro}
            nuevos_datos = {}
            
            if nuevo_nombre:
                nuevos_datos["nombre"] = nuevo_nombre
            if nueva_edad:
                nuevos_datos["edad"] = int(nueva_edad)
            if nuevo_email:
                nuevos_datos["email"] = nuevo_email
            if nueva_direccion:
                nuevos_datos["direccion"] = nueva_direccion
            if nuevo_telefono:
                nuevos_datos["telefono"] = nuevo_telefono
            
            # Llamamos a la función de actualización
            pacientes_modificados = actualizar_paciente(db, filtro, nuevos_datos)
            if pacientes_modificados > 0:
                print(f"{pacientes_modificados} paciente(s) actualizado(s).")
            else:
                print("No se encontró el paciente o no hubo cambios.")
        
        elif opcion == '4':
            print("Actualizar varios pacientes por nombre")
            nombre_filtro = input("Ingrese el nombre de los pacientes que desea actualizar: ")
            
            nuevo_telefono = input("Nuevo teléfono para los pacientes seleccionados: ")
            nuevo_email = input("Nuevo email para los pacientes seleccionados: ")

            # Filtro para seleccionar los pacientes por nombre
            filtro = {"nombre": nombre_filtro}
            nuevos_datos = {}

            if nuevo_telefono:
                nuevos_datos["telefono"] = nuevo_telefono
            if nuevo_email:
                nuevos_datos["email"] = nuevo_email
            
            pacientes_modificados = actualizar_varios_pacientes(db, filtro, nuevos_datos)
            print(f"{pacientes_modificados} paciente(s) actualizado(s).")
        
        elif opcion == '5':
            print("Obtener varios pacientes por filtro")
            atributo_filtro = input("Ingrese el atributo que desea filtrar (por ejemplo, 'edad', 'nombre', etc.): ")
            valor_filtro = input(f"Ingrese el valor para filtrar por {atributo_filtro}: ")
            if atributo_filtro == 'edad':
                valor_filtro = int(valor_filtro)
            
            # Creamos el filtro dinámicamente
            filtro = {atributo_filtro: valor_filtro}
            pacientes = obtener_varios_registros(db, filtro)
            
            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes:")
                for paciente in pacientes:
                    print(paciente)
            else:
                print("No se encontraron pacientes que coincidan con el filtro.")
        
        elif opcion == '6':
            print("Obtener varios pacientes por filtro con varios atributos")
            # Crear un filtro con varios atributos
            filtro = {}
            
            nombre_filtro = input("¿Deseas filtrar por nombre? (sí/no): ")
            if nombre_filtro.lower() == "sí" or nombre_filtro.lower() == "si" or nombre_filtro.lower() == "s":
                nombre = input("Ingrese el nombre para filtrar: ")
                filtro["nombre"] = nombre
            
            edad_filtro = input("¿Deseas filtrar por edad? (sí/no): ")
            if edad_filtro.lower() == "sí" or edad_filtro.lower() == "si" or edad_filtro.lower() == "s":
                edad = input("Ingrese la edad para filtrar: ")
                filtro["edad"] = edad
            
            email_filtro = input("¿Deseas filtrar por email? (sí/no): ")
            if email_filtro.lower() == "sí" or email_filtro.lower() == "si" or email_filtro.lower() == "s":
                email = input("Ingrese el email para filtrar: ")
                filtro["email"] = email
            
            pacientes = obtener_varios_registros_por_filtro_multiple(db, filtro)
            
            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes:")
                for paciente in pacientes:
                    print(paciente)
            else:
                print("No se encontraron pacientes que coincidan con el filtro.")
        
        elif opcion == '7':
            print("Obtener pacientes sin valores nulos en un atributo")
            atributo = input("Ingrese el nombre del atributo (por ejemplo, 'email', 'telefono', etc.): ")
            pacientes = obtener_registros_no_nulos(db, atributo)
            
            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes sin valores nulos en el atributo '{atributo}':")
                for paciente in pacientes:
                    print(paciente)
            else:
                print(f"No se encontraron pacientes con el atributo '{atributo}' sin valores nulos.")
        
        elif opcion == '8':
            print("Obtener pacientes sin un atributo específico")
            atributo = input("Ingrese el nombre del atributo (por ejemplo, 'email', 'telefono', etc.): ")
            pacientes = obtener_registros_sin_atributo(db, atributo)
            
            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes sin el atributo '{atributo}':")
                for paciente in pacientes:
                    print(paciente)
            else:
                print(f"No se encontraron pacientes sin el atributo '{atributo}'.")
        
        elif opcion == '9':
            print("Obtener pacientes por lista de valores en un atributo")
            atributo = input("Ingrese el nombre del atributo (por ejemplo, 'edad', 'nombre', etc.): ")
            valores = input("Ingrese los valores para filtrar (separados por coma): ")
            
            # Convertir la entrada de valores a una lista
            # si el valor es edad hacer int(valor )
            if atributo == 'edad':
                lista_valores = [int(valor.strip()) for valor in valores.split(",")]
            else:
                lista_valores = [valor.strip() for valor in valores.split(",")]
            
            pacientes = obtener_registros_por_lista_de_valores(db, atributo, lista_valores)
            
            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes con los valores especificados en '{atributo}':")
                for paciente in pacientes:
                    print(paciente)
            else:
                print(f"No se encontraron pacientes con los valores especificados en '{atributo}'.")
        
        elif opcion == '10':
            print("Obtener pacientes con un atributo numérico mayor que el valor especificado")
            atributo = input("Ingrese el nombre del atributo numérico (por ejemplo, 'edad', 'telefono', etc.): ")
            valor = float(input(f"Ingrese el valor umbral para el atributo {atributo}: "))
            
            pacientes = obtener_registros_mayores(db, atributo, valor)
            
            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes con el atributo '{atributo}' mayor que {valor}:")
                for paciente in pacientes:
                    print(paciente)
            else:
                print(f"No se encontraron pacientes con el atributo '{atributo}' mayor que {valor}.")
        
        elif opcion == '11':
            print("Obtener pacientes con condición 'u otra' (operador OR)")

            # Solicitar los filtros (atributo y valor) para las condiciones
            filtros = []
            while True:
                atributo = input("Ingrese el atributo (por ejemplo, 'edad', 'nombre', etc.) para una condición: ")
                valor = input(f"Ingrese el valor para el atributo '{atributo}': ")

                # Convierte el valor a int si es un número (por ejemplo, edad)
                if atributo == "edad":
                    valor = int(valor)

                # Añadir la condición a la lista de filtros
                filtros.append({atributo: valor})
                
                continuar = input("¿Desea agregar otra condición (sí/no)? ")
                if continuar.lower() != 'sí' and continuar.lower() != 'si':
                    break

            # Llamar a la función para obtener los registros con la condición OR
            pacientes = obtener_registros_condicion_u_otra(db, filtros)

            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes que cumplen al menos una de las condiciones:")
                for paciente in pacientes:
                    print(paciente)
            else:
                print("No se encontraron pacientes que cumplan con las condiciones.")
                
        elif opcion == '12':
            print("Obtener pacientes que no cumplan una condición específica")

            # Solicitar el atributo y valor para el filtro
            atributo = input("Ingrese el atributo (por ejemplo, 'edad', 'nombre', etc.): ")
            valor = input(f"Ingrese el valor para el atributo '{atributo}' que no debe coincidir: ")

            # Convertir el valor a int si es un número (por ejemplo, edad)
            if atributo == "edad":
                valor = int(valor)

            # Llamar a la función para obtener los registros que no cumplan con la condición
            pacientes = obtener_registros_no_cumple_condicion(db, atributo, valor)

            if pacientes:
                print(f"Se encontraron {len(pacientes)} pacientes que no cumplen con la condición {atributo} != {valor}:")
                for paciente in pacientes:
                    print(paciente)
            else:
                print(f"No se encontraron pacientes que no cumplan con la condición {atributo} != {valor}.")
        
        elif opcion == '13':
            print("Eliminar un registro de la colección")

            # Solicitar los datos para identificar el registro a eliminar
            nombre_filtro = input("Ingrese el nombre del paciente que desea eliminar: ")

            # Crear el filtro para encontrar el paciente por nombre
            filtro = {"nombre": nombre_filtro}
            
            # Llamar a la función de eliminación
            registros_eliminados = eliminar_registro(db, filtro)
            
            if registros_eliminados > 0:
                print(f"{registros_eliminados} paciente(s) eliminado(s).")
            else:
                print(f"No se encontró ningún paciente con el nombre '{nombre_filtro}' o ya fue eliminado.")
        
        elif opcion == '14':
            print("Eliminar varios registros de la colección")

            # Solicitar el filtro para eliminar los registros
            atributo_filtro = input("Ingrese el atributo por el que desea filtrar (por ejemplo, 'edad', 'nombre'): ")
            valor_filtro = input(f"Ingrese el valor para filtrar por {atributo_filtro}: ")
            
            if atributo_filtro == 'edad':
                # Si el atributo es 'edad', convertimos el valor a entero
                valor_filtro = int(valor_filtro)
            
            # Crear el filtro para eliminar varios registros
            filtro = {atributo_filtro: valor_filtro}
            
            # Llamar a la función para eliminar los registros
            registros_eliminados = eliminar_varios_registros(db, filtro)
            
            if registros_eliminados > 0:
                print(f"{registros_eliminados} paciente(s) eliminado(s).")
            else:
                print(f"No se encontraron pacientes con el filtro '{atributo_filtro}: {valor_filtro}' o ya fueron eliminados.")
        
        elif opcion == '15':
            print("Realizar una búsqueda y ordenarla de forma ascendente")

            # Solicitar al usuario el atributo por el que desea ordenar
            atributo_ordenar = input("Ingrese el atributo por el cual desea ordenar (por ejemplo, 'edad', 'nombre', etc.): ")

            # Obtener los registros ordenados
            registros_ordenados = obtener_registros_ordenados(db, atributo_ordenar)
            
            if registros_ordenados:
                print(f"Se encontraron {len(registros_ordenados)} pacientes ordenados por {atributo_ordenar} de forma ascendente:")
                for paciente in registros_ordenados:
                    print(paciente)
            else:
                print(f"No se encontraron pacientes con el atributo '{atributo_ordenar}'.")
        
        elif opcion == '16':
            print("Realizar una búsqueda y ordenarla de forma descendente")

            # Solicitar al usuario el atributo por el que desea ordenar
            atributo_ordenar = input("Ingrese el atributo por el cual desea ordenar (por ejemplo, 'edad', 'nombre', etc.): ")

            # Obtener los registros ordenados de manera descendente
            registros_ordenados_descendente = obtener_registros_ordenados_descendente(db, atributo_ordenar)
            
            if registros_ordenados_descendente:
                print(f"Se encontraron {len(registros_ordenados_descendente)} pacientes ordenados por {atributo_ordenar} de forma descendente:")
                for paciente in registros_ordenados_descendente:
                    print(paciente)
            else:
                print(f"No se encontraron pacientes con el atributo '{atributo_ordenar}'.")
        
        elif opcion == '17':
            print("Realizar una búsqueda limitada a 10 registros")
            
            # Obtener los primeros 10 registros
            registros_limitados = obtener_primeros_10_registros(db)
            
            if registros_limitados:
                print(f"Se encontraron {len(registros_limitados)} registros limitados:")
                for paciente in registros_limitados:
                    print(paciente)
            else:
                print("No se encontraron registros.")
        
        elif opcion == '18':
            print("Realizar una búsqueda por expresión regular")
            
            # Solicitar al usuario el campo y el patrón de búsqueda
            campo = input("Ingrese el campo en el que desea realizar la búsqueda (por ejemplo, 'nombre', 'email'): ")
            patron = input("Ingrese la expresión regular para filtrar (puede usar * o ? como comodines): ")
            
            # Llamar a la función de búsqueda por expresión regular
            registros_regex = obtener_registros_por_regex(db, campo, patron)
            
            if registros_regex:
                print(f"Se encontraron {len(registros_regex)} registros que coinciden con el patrón '{patron}':")
                for paciente in registros_regex:
                    print(paciente)
            else:
                print(f"No se encontraron registros que coincidan con el patrón '{patron}'.")
                
        elif opcion == '19':
            # Filtrar enfermedades por síntomas
            print("Filtrar enfermedades por síntomas")
            sintomas = input("Ingrese los síntomas a filtrar (separados por coma): ")
            
            # Convertir la entrada de síntomas a una lista
            lista_sintomas = [sintoma.strip() for sintoma in sintomas.split(",")]
            
            # Llamamos a la función para obtener las enfermedades
            enfermedades = obtener_enfermedades_por_sintomas(db, lista_sintomas)
            
            if enfermedades:
                print(f"Se encontraron {len(enfermedades)} enfermedades con los síntomas proporcionados:")
                for enfermedad in enfermedades:
                    print(enfermedad)
            else:
                print("No se encontraron enfermedades con los síntomas proporcionados.")
        
        elif opcion == '21':
            # Insertar una nueva enfermedad
            print("Insertar una nueva enfermedad")
            
            nombre = input("Nombre de la enfermedad: ")
            descripcion = input("Descripción de la enfermedad: ")
            sintomas = input("Síntomas de la enfermedad (separados por coma): ")
            
            # Convertir los síntomas a una lista
            lista_sintomas = [sintoma.strip() for sintoma in sintomas.split(",")]
            
            tratamiento = input("Tratamiento recomendado (opcional): ")
            if tratamiento == "":
                tratamiento = None  # Si no se proporciona un tratamiento, se establece como None
            
            # Llamamos a la función para insertar la enfermedad en la base de datos
            enfermedad_id = insertar_enfermedad(db, nombre, descripcion, lista_sintomas, tratamiento)
            print(f"Enfermedad insertada con ID: {enfermedad_id}")
        
        elif opcion == '22':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
