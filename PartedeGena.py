import os
os.system("cls")
a= input("¿Que vas a calcular?(Cantidad de concreto en m3/Mamposteria/Piso/Techo):")

if a == "Mamposteria":
    b = float(input("Ingrese el ancho de la pared:"))
    c = float(input("Ingrese el alto de la pared:"))
    d = input("Ingrese el tipo de ladrillo:(King Kong/Pandereta)")
    if d == "King Kong":
        cl = (b*c)/((0.24 + 0.015)*(0.09+ 0.015))
        cl1 = cl + (cl*0.05)
        x = round(cl1,0)
        y = round(cl,0)
        vmo = (b*c*0.13)-(y*0.09*0.13*0.24)
        cemento = (vmo * 7.5)/(b*c)
        arena_gruesa = (vmo*1.05)/(b*c)
        cem = round(cemento,2)
        are = round(arena_gruesa,2)
        print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")
        print("La cantidad de bolsas de cemento es",cem, "m3")
        print("La cantidad de arena guesa es",are,"m3")
        
    elif d == "Pandereta":
        e = input("El tipo de aparejo sera:(Soga/Cabeza)")
        cl = (b*c)/((0.24 + 0.015)*(0.09+ 0.015))
        cl1 = cl + (cl*0.05)
        x = round(cl1,0)
        y = round(cl,0)
        vmo = (b*c*0.13)-(y*0.09*0.13*0.24)
        cemento = (vmo * 7.5)/(b*c)
        arena_gruesa = (vmo*1.05)/(b*c)
        cem = round(cemento,2)
        are = round(arena_gruesa,2)
        print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")
        print("La cantidad de bolsas de cemento es",cem, "m3")
        print("La cantidad de arena guesa es",are,"m3")
    
#calculo del area de techo
elif a == "Techo de losa":
    ancho = float(input("Ingrese el ancho:"))   # ancho de techo
    largo = float(input("Ingrese el largo:"))   #longitud de techo
    espesor = float(input("Ingrese espesor de ladrillo:"))                            
    area = ancho * largo
    volumen = area * espesor

#calculo de la cantidad de ladrillos
    tipoladrillo = input("Tipo de ladrillo:")
    vigueta = float(input("Ingrese ancho de Vigueta:")) #la vigueta es el relleno que existe entre los ladrillos

    if tipoladrillo == "king kong":
        cantidadladrillos = area/((13 + vigueta)*24)
        volumenladrillos = 0.002808
    elif tipoladrillo == "Pandereta":
        cantidadladrillos = area/((12 + vigueta)*24)
        volumenladrillos = 0.002592
    else:
        ancholadrillo = float(input("Ingrese ancho de ladrillo:"))
        longitudladrillo = float(input("Ingrese longitud de ladrillo:"))

        cantidadladrillos = area/((ancholadrillo + vigueta)*longitudladrillo)
        alturaladrillo = 0.12
        volumenladrillos = ancholadrillo * longitudladrillo * alturaladrillo

#calulo de volumen de concreto    
    cantidadconcreto = volumen - (cantidadladrillos * volumenladrillos)

#Resultados
    print(volumen,"metros cubicos de techo")
    print(cantidadladrillos, "ladrillos")
    print(cantidadladrillos,"ladrillos en total para",volumen,"metros cubicos")
    print(cantidadconcreto,"metros cubicos por metro cuadrado")

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


