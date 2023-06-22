



clientes = []

def validar_rut(rut):
    return rut.isalnum() and 8 <= len(rut) <= 9

def mostrar_menu():
    print("**********menu pincipal**********")
    print("1) Registrar")
    print("2) Buscar por Rut")
    print("3) Reporte según renta")
    print("4) Salir")
    print("************************************")

def registrar_cliente():
    
    rut = input("Ingrese el Rut del cliente  (sin puntos ni guion) : ")
    while not validar_rut(rut):
        print("Rut inválido. Intente nuevamente.")
        rut = input("Ingrese el Rut del cliente: ")
    
    nombre = input("Ingrese el Nombre del cliente: ")
    print("escriba el proyecto en mayusculas gracias por mantener el orden")
    print(f"los terminos utilisados son\nVS:vive en santiago \nVF:vive en la florida \nVN:vive en ñuñoa")
    proyecto = input("Ingrese el Proyecto (VS, VF o VN): ")
    
    renta = int(input("Ingrese la Renta Mensual del cliente: "))
    
    cliente = {
        "Rut": rut,
        "Nombre": nombre,
        "Proyecto": proyecto,
        "Renta": renta
    }
    clientes.append(cliente)
    print("Cliente registrado exitosamente.")

def buscar_cliente_por_rut():
    rut = input("Ingrese el Rut del cliente: ")
    for cliente in clientes:
        if cliente["Rut"] == rut:
            encontrado = True
            print("* Datos del Cliente*")
            print(f"Rut: {cliente['Rut']}")
            print(f"Nombre: {cliente['Nombre']}")
            print(f"Proyecto: {cliente['Proyecto']}")
            print(f"Renta Mensual: {cliente['Renta']}")
        else:
            print("rut no registrado")
            print("retornando al menu")

def generar_reporte_renta_superior():
    reportes_generados = 0
    print("Reportes")
    for cliente in clientes:
        if cliente["Renta"] >= 900000:
            reportes_generados += 1
            nombre = cliente["Nombre"]
            rut = cliente["Rut"]
            renta = cliente["Renta"]
            proyecto = cliente["Proyecto"]
        import random
        for x in range(1): 
            dpto_uf = random.randint(2500, 3700)
            print("************reporte************")
            print(f"cliente: {nombre}")
            print(f"Rut: {rut}")
            print(f"Con su renta de {renta}")
            print(f"En el Proyecto: {proyecto}")
            print(f"Puede acceder a un Dpto de UF: {dpto_uf}")
            print("********************************")
    
    print(f"Se generaron {reportes_generados} reportes.")
    print("recuerde que solamente se generan reportes para rentas iguales o superiores a los $900000")

while True:
    mostrar_menu()
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        buscar_cliente_por_rut()
    elif opcion == "3":
        generar_reporte_renta_superior()
    elif opcion == "4":
        print("finalizando del programa")
        break
    else:
        print("Opción inválida. Intente nuevamente.")