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
        print("11. Salir")
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
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida.")