from mysql.connector import Error
from LN.bodegaClass import obtener_bodegas
from LN.productoClass import obtener_productos


def menuPrincipal():
    while True:
        print('================MENU PRINCIPAL================')
        print('1.- Listar ')
        print('2.- Registrar')
        print('3.- Actualizar')
        print('4.- Eliminar')
        print('5.- Salir')
        print('==============================================')
        opcion = int(input('Seleccione una opcion: '))

        if opcion < 1 or opcion > 5:
            print("Opcion incorrecta, ingrese nuevamente...")
        else:
            if opcion == 1:
                opcion_listar = int(input('Que informacion desea listar   1)Bodegas 2)Productos: '))
                if opcion_listar == 1:
                    try:
                        bodegas = obtener_bodegas()
                        for bodega in bodegas:
                            print("ID: ", bodega.Idbodega)
                            print("Nombre: ", bodega.Nombre)
                            print("Dirección: ", bodega.Direccion)
                            print("Jefe Asignado: ", bodega.Jefeasignado)
                            print("Capacidad: ", bodega.Capacidad)
                            print("Nivel de Ocupación: ", bodega.Niveldeocupacion)
                            print("Correo Bodega: ", bodega.Correobodega)
                            print("Número Fijo: ", bodega.Numerofijo)
                            print("")

                        realizar_otra_opcion = input("¿Desea realizar otra opción? (S/N): ")
                        if realizar_otra_opcion.upper() != "S":
                            break
                    except Error as ex:
                        print("Ocurrio un error...")
                        print("Error capturado: {}".format(ex))

                elif opcion_listar == 2:
                    try:
                        productos = obtener_productos()
                        for producto in productos:
                            print("ID: ", producto.Idproducto)
                            print("ID: ", producto.Id_editorial)
                            print("Fechaing: ", producto.Fechaing)
                            print("Cantidades: ", producto.Cantidades)
                            print("Tipo de producto: ", producto.Tipoproducto)
                            print("")

                        realizar_otra_opcion = input("¿Desea realizar otra opción? (S/N): ")
                        if realizar_otra_opcion.upper() != "S":
                            break
                    except Error as ex:
                        print("Ocurrio un error...")
                        print("Error capturado: {}".format(ex))
            elif opcion == 2:
                print("Aquí va crear")
            elif opcion == 3:
                print("Aquí va actualizar")
            elif opcion == 4:
                pass
            else:
                print("!Gracias por usar este sistema!")
                break


menuPrincipal()