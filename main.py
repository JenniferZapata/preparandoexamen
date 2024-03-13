bandas=[]


#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):

    print("1. Registrar Banda")
    print("2. Buscar Información de una Bandaa")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. Salir")

    opcion=int(input("Digita una opción: "))

    if opcion==1:
        banda={}
        #Creando datos del diccionario
        banda["id"]=int(input("Digital el id: "))
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero ")
        banda["clasificacion"]=input("Clasificación 5")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Costo: ($)"))
        
        #Agregando un diccionario a una lista
        bandas.append(banda)
    elif opcion==2:
        bandaBuscada=input("Digita el nombre de la banda que estas buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandaBuscada:
                #Como lo encontre, muestro los datos de la bandAuxiliar
                print(F"id: {bandAuxiliar["id"]}---- nombre:{bandAuxiliar["nombre"]}")
            else:
                print("Sigue buscando...")
    elif opcion==3:
        print(bandas)
    elif opcion==4:
        
    elif opcion==5:
        pass    
    else:
        pass    

