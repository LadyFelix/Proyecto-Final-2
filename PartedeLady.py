
a= input("¿Que vas a calcular?(Capa Aisladora/Mamposteria/Piso/Techo)")
if a == "Capa Aisladora":
    b = input("Ingrese el tipo de capa aisladora: (Horizontal/Vertical)")
    c = float(input("Ingrese el ancho del muro en metros:"))
    d = float(input("Ingrese el largo del muro en metros:"))
    volumen = c * d * 0.02
    x = volumen * 10,8
    print(x)