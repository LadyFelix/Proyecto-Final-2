import os
os.system("cls")

a= input("¿Que vas a calcular?(Capa Aisladora/Mamposteria/Piso/Techo)")
if a == "Capa Aisladora":
    b = input("Ingrese el tipo de capa aisladora: (Horizontal/Vertical)")
    c = float(input("Ingrese el ancho del muro en metros:"))
    d = float(input("Ingrese el largo del muro en metros:"))
    volumen = c * d * 0.02
    x = (volumen * 10.8)
    print("Cemento:",x,"Kg")

elif a == "Mamposteria":
    b = int(input("Ingrese el ancho de la pared:"))
    c = int(input("Ingrese el alto de la pared:"))
    d = input("Ingrese el tipo de ladrillo:(King Kong/Pandereta)")
    if d == "King Kong":
        e = input("El tipo de aparejo sera:(Soga/Cabeza)")
        if e == "Soga":
            cl = (b*c)/((0.24 + 0.015)*(0.09+ 0.015))
            cl1 = cl + (cl*0.05)
            x = round(cl1,0)
            y = round(cl,0)
            vmo = (b*c*0.13)-(y*0.09*0.13*0.24)
            print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")
            print("La cantidad de bolsas de cemento es", vmo*7.5)
            print("La cantidad de arena guesa es",vmo*1.05)
        elif e =="Cabeza":
            cl = (b*c)/((0.13 + 0.015)*(0.09+ 0.015))
            cl1 = cl + (cl1*0.05)
            x = round(cl1,0)
            print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")
    elif d == "Pandereta":
        e = input("El tipo de aparejo sera:(Soga/Cabeza)")
        if e == "Soga":
            cl = (b*c)/((0.24 + 0.015)*(0.09+ 0.015))
            cl1 = cl + (cl*0.05)
            x = round(cl1,0)
            print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")
        elif e =="Cabeza":
            cl = (b*c)/((0.12 + 0.015)*(0.09+ 0.015))
            cl1 = cl + (cl*0.05)
            x = round(cl1,0)
            print("La cantidad de ladrillos es",x,"considerando el 5% de desperdicio")


x= float(input("Registrar ancho del piso en cm"))
y= float(input("Registrar largo del piso en cm"))
lo= float(input("Registre ancho de loza en cm"))
sa= float(input("Registre largo de loza en cm"))
#Numero de piezas
t= (x*y)
l=(lo*sa)
u=t/l
w= round(u,0)
print("Losas requeridas", w)
#Cuantas losas adicional/10% de desperdicio
g= w*0.01 
h= round(g,0)
print("Losas adicionales", h)
#Losas en total
r= u+h
p= round(r,0)
print("En total necesitaremos",p, "losas")