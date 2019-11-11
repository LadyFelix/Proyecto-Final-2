import os
os.system("cls")

a= input("¿Que vas a calcular?(Capa Aisladora/Mamposteria/Piso/Techo):")
if a == "Capa Aisladora":
    b = input("Ingrese el tipo de capa aisladora: (Horizontal/Vertical)")
    c = float(input("Ingrese el ancho del muro en metros:"))
    d = float(input("Ingrese el largo del muro en metros:"))
    volumen = c * d * 0.02
    x = (volumen * 10.8)
    print("Cemento:",x,"Kg")

elif a == "Mamposteria":
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
    
elif a == "Techo de losa":
    ancho = float(input("Ingrese el ancho:"))   # ancho de techo
    largo = float(input("Ingrese el largo:"))   #longitud de techo
    espesor = 0.25                              # espesor fijo de techo
    area = ancho * largo
    volumen = area * espesor

    cantidadladrillos = input("Tipo de ladrillo:")
    vigueta = float(input("Ingrese ancho de Vigueta:")) #la vigueta es el relleno que existe entre los ladrillos

    if cantidadladrillos == "king kong":
        cantidadladrillos = area/((13 + vigueta)*24)
    elif cantidadladrillos == "Pandereta":
        cantidadladrillos = area/((12 + vigueta)*24)
    else:
        ancholadrillo = float(input("Ingrese ancho de ladrillo:"))
        longitudladrillo = float(input("Ingrese longitud de ladrillo:"))
    
        cantidadladrillos = area/((ancholadrillo + vigueta)*longitudladrillo)


    print(volumen,"metros cubicos de techo")
    print(cantidadladrillos, "ladrillos")
    print(cantidadladrillos,"ladrillos en total para",volumen,"metros cubicos")
