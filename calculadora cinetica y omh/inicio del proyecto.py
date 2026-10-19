print("==================================")
print("MENU PRINCIPAL")
print("==================================")
programa_activo = True
while programa_activo:
    opciones = ["ley de omh", "cinetica"]
    print(opciones)
    seleccion = int(input("escrive 1 para ley de omh y 2 para cinetica: "))
    if seleccion == 1:
        print("BIENVENIDO A LA CALCULADORA DE LEY DE omh")
        opcion_1 = ["1. corriente", "2. resistencia", "3. voltaje", "4 MENU PRINCIPAL"]
        print(opcion_1)
        ley_omh_activa = True
        while ley_omh_activa:
            seleccion_de_formula = int(input("ingrese el numero de la opcion deseada 1, 2, 3, 4: "))
            if seleccion_de_formula == 1:
                print("ingresa los datos que se te piden")
                voltaje = float(input("ingrese el voltaje en voltios: "))
                resistencia = float(input("ingresa la resistencia en omh's: "))
                print(opcion_1)
                if resistencia == 0:
                    print("la operacion no es valida cheque la corriente")
                else:
                    corriente = voltaje / resistencia
                    print("la corriente es de: ", corriente, "amperes")
                    print(opcion_1)
                    if opcion_1 == True:
                       print(seleccion_de_formula)          
            elif seleccion_de_formula == 2:
                print("ingrese los datos que se le piden")
                voltaje = float(input("ingrese el voltaje en voltios: "))
                corriente = float(input("ingrese la corriente en amperes: "))
                if corriente == 0:
                    print("no se puede realizar la operacion cheque el valor de la corriente")
                else:
                    resistencia = voltaje / corriente
                    print("la resistencia es de: ", resistencia, "omh's")
                    print(opcion_1)
                    if opcion_1 == True:
                       print(seleccion_de_formula)
            elif seleccion_de_formula == 3:
                print("ingrese los datos que se le piden")
                resistencia = float(input("ingrese la resistencia en ohm's: "))
                corriente = float(input("ingrese la corriente en amperes: "))
                if corriente == 0:
                    print("el sircuito no esta funcionando")
                elif resistencia == 0:
                    print("no hay caida de tencion")
                else:
                    voltaje = corriente * resistencia
                    print("el voltaje es de: ", voltaje, "voltio")
                    print(opcion_1)
                    if opcion_1 == True:
                        print(seleccion_de_formula)
            elif seleccion_de_formula == 4:
                print("resgresa al menu")
                ley_omh_activa = False
            else:
                print("Esta opcion no existe")
    elif seleccion == 2:
        print("BIENVENIDO A CALCULADORA DE CINETICA")
        opcion2 = ["1 velocidad", "2 distancia", "3 tiempo", "4 MENU PRINCIPAL"]
        print(opcion2)
        calculo_cinetica_activa = True
        while calculo_cinetica_activa:
            seleccion_de_formula_2 = int(input("ingrese el numero de la opcion deseada 1, 2, 3 o 4: "))
            if seleccion_de_formula_2 == 1:
                print("ingrese los datos que le piden")
                distancia = float(input("ingrese la distancia en metros: "))
                tiempo = float(input("ingrese el tiempo en segundos: "))
                if tiempo == 0:
                    print("la operacion no se puede realizar cheque el tiempo ingresado")
                else:
                    velocidad = distancia / tiempo
                    print("la velocidad es de: ", velocidad, "m/s")
                    print(opcion2)
                    if opcion2 == True:
                        print(seleccion_de_formula_2)
            elif seleccion_de_formula_2 == 2:
                print("ingresa los datos que se te piden")
                velocidad = float(input("ingrese la velocidad en m/s: "))
                tiempo = float(input("ingrese el tiempo en segundos: "))
                distancia = velocidad * tiempo
                print("la distancia es de: ", distancia, "metros")
                print(opcion2)
                if opcion2 == True:
                    print(seleccion_de_formula_2)
            elif seleccion_de_formula_2 == 3:
                print("ingrese los datos que se le piden")
                velocidad = float(input("ingrese la velocidad en m/s: "))
                distancia = float(input("ingrese la distancia en metros: "))
                if distancia == 0:
                    print("la operacion no se puede realizar cheque la distancia")
                else:
                    tiempo = velocidad / distancia
                    print("el tiempo es de: ", tiempo, "segundos")
                    print(opcion2)
                    if opcion2 == True:
                        print(seleccion_de_formula_2)
            elif seleccion_de_formula_2 == 4:
                print("regresa al MENU PRINCIPAL")
                calculo_cinetica_activa = False
            else:
                print("esta opcion no exista")
#Grasias Dios gloria a ti señor que medas manos para programar, grasias a mis amigos que desde la infancia creyeron en mi y a mis abuelitos 