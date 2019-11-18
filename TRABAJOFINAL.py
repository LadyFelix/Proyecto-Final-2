import os
os.system("cls")
while True:
    a= input("¿Que vas a calcular?(Mamposteria/Techo/Piso/Tarrajeo):")

    #Calculo de area en mamposteria
    if a == "Mamposteria":
        b = float(input("Ingrese el ancho de la pared:"))
        c = float(input("Ingrese el alto de la pared:"))
        
        
    #Calculo de ladrillos, cemento y arena gruesa en una mamposteria 
        while True:
            d = input("Ingrese el tipo de ladrillo:(King Kong/Pandereta)")
            if d == "King Kong":
                cl = (b*c)/((0.24 + 0.015)*(0.09+ 0.015))
                cl1 = cl + (cl*0.05)
                x = round(cl1,0)
                y = round(cl,0)
                vmo = (b*c*0.13)-(y*0.09*0.13*0.24)
                cemento = (vmo * 7.5)
                arena_gruesa = (vmo*1.05)
                cem = round(cemento,0)
                are = round(arena_gruesa,2)
                print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")
                print("La cantidad de bolsas de cemento es",cem)
                print("La cantidad de arena gruesa es",are,"m3")
                break
                
            elif d == "Pandereta":
                
                cl = (b*c)/((0.24 + 0.015)*(0.09+ 0.015))
                cl1 = cl + (cl*0.05)
                x = round(cl1,0)
                y = round(cl,0)
                vmo = (b*c*0.13)-(y*0.09*0.13*0.24)
                cemento = (vmo * 7.5)
                arena_gruesa = (vmo*1.05)
                cem = round(cemento,0)
                are = round(arena_gruesa,2)
                print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")
                print("La cantidad de bolsas de cemento es",cem)
                print("La cantidad de arena guesa es",are,"m3")
                break
            
        
    #calculo del area de techo
    elif a == "Techo":

        ancho = float(input("Ingrese el ancho en m:"))   # ancho de techo
        largo = float(input("Ingrese el largo en m:"))   #longitud de techo
        espesor = float(input("Ingrese espesor de techo en m:"))                            
        area = ancho * largo
        volumen = area * espesor

    #calculo de la cantidad de ladrillos
        tipoladrillo = input("Tipo de ladrillo:(Ladrillo 1/ Ladrillo 2/ Ninguno)")
        vigueta = float(input("Ingrese ancho de Vigueta:")) #la vigueta es el relleno que existe entre los ladrillos

        if tipoladrillo == "Ladrillo 1":
            cantidadladrillos = area/((0.30 + vigueta)*0.30)
            volumenladrillos = 0.0108
        elif tipoladrillo == "Ladrillo 2":
            cantidadladrillos = area/((0.30 + vigueta)*0.30)
            volumenladrillos = 0.0135
        else:
            ancholadrillo = float(input("Ingrese ancho de ladrillo:"))
            longitudladrillo = float(input("Ingrese longitud de ladrillo:"))

            cantidadladrillos = area/((ancholadrillo + vigueta)*longitudladrillo)
            alturaladrillo = 0.12
            volumenladrillos = ancholadrillo * longitudladrillo * alturaladrillo

    #calulo de volumen de concreto    
        cantidadconcreto = volumen - (cantidadladrillos * volumenladrillos)
        vol = round(volumen,0)
        cant1 = round(cantidadladrillos,0)
        cnt2 = round(cantidadconcreto,2)

    #Resultados
        
        print(cant1,"ladrillos en total para",vol,"metros cubicos de techo")
        print(cnt2,"metros cubicos de concreto por metro cuadrado")

    elif a== "Piso":

        an=float(input("Registrar ancho del piso en cm"))
        la= float(input("Registrar largo del piso en cm"))
        lo= float(input("Registrar ancho de la losa en cm"))
        sa= float(input("Registrar largo de la losa en cm"))
        #Numero de piezas
        t= (an*la)
        l=(lo*sa)
        u=t/l
        w= round(u,0)
        print("Losas requeridas",w)
        #Cuantas losas adicional/10% de desperdicio
        g= w*0.01
        h= round(g,0)
        print("Lozas adicionales", h)
        #Losas en total
        r=u+h
        p= round(r,0)
        print("En total necesitaremos",p , "lozas")

    elif a== "Tarrajeo":
        ancho= float(input("Registrar ancho de la pared en m"))
        largo= float(input("Registrar largo de la pared en m"))
        areaa= ancho*largo
        #Tarrajeo por m2
        #Cemento 0.14 bolsa
        #Arena fina 0.03 m3
        cemento= 0.14*areaa
        arena= 0.03*areaa
        print("Cemento", cemento, "bolsas y Arena fina", arena, "m3")
