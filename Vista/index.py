from tkinter import Tk, Label, Button, Entry, Scrollbar, Text, Frame
from LN.bodegaClass import obtener_bodegas, guardar_bodega,actualizar_bodega
from LN.productoClass import obtener_productos, guardar_producto,actualizar_producto
from datetime import datetime


# Función para mostrar datos de bodega
def mostrar_bodega():
    # Crear ventana secundaria para mostrar los datos de la bodega
    ventana_mostrar = Tk()
    ventana_mostrar.title("Bodegas")

    # Crear un widget Text para mostrar los datos
    texto = Text(ventana_mostrar, height=10, width=50)
    texto.pack(side="left", fill="both", expand=True)

    # Crear un scrollbar para desplazarse por los datos
    scrollbar = Scrollbar(ventana_mostrar)
    scrollbar.pack(side="right", fill="y")

    # Asociar el scrollbar con el widget Text
    texto.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=texto.yview)

    # Obtener los datos de las bodegas
    bodegas = obtener_bodegas()

    # Agregar los datos al widget Text
    for i, bodega in enumerate(bodegas):
        texto.insert("end", "ID: " + str(bodega.Idbodega) + "\n")
        texto.insert("end", "Nombre: " + bodega.Nombre + "\n")
        texto.insert("end", "Dirección: " + bodega.Direccion + "\n")
        texto.insert("end", "Jefe asignado: " + bodega.Jefeasignado + "\n")
        texto.insert("end", "Capacidad: " + str(bodega.Capacidad) + "\n")
        texto.insert("end", "Nivel de ocupación: " + str(bodega.Niveldeocupacion) + "\n")
        texto.insert("end", "Correo Bodega: " + str(bodega.Correobodega) + "\n")
        texto.insert("end", "Número Fijo: " + str(bodega.Numerofijo) + "\n")

        # Agrega aquí los datos adicionales de la bodega

        # Separador entre bodegas
        if i < len(bodegas) - 1:
            texto.insert("end", "------------------------\n")

    # Desactivar la edición del widget Text
    texto.config(state="disabled")

    # Ejecutar ventana secundaria
    ventana_mostrar.mainloop()


# Función para mostrar datos de producto
def mostrar_producto():
    # Crear ventana secundaria para mostrar los datos de la bodega
    ventana_mostrar = Tk()
    ventana_mostrar.title("Bodegas")

    # Crear un widget Text para mostrar los datos
    texto = Text(ventana_mostrar, height=10, width=50)
    texto.pack(side="left", fill="both", expand=True)

    # Crear un scrollbar para desplazarse por los datos
    scrollbar = Scrollbar(ventana_mostrar)
    scrollbar.pack(side="right", fill="y")

    # Asociar el scrollbar con el widget Text
    texto.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=texto.yview)

    # Obtener los datos de las bodegas
    productos = obtener_productos()

    # Agregar los datos al widget Text
    for i, producto in enumerate(productos):
        texto.insert("end", "ID Producto: " + str(producto.Idproducto) + "\n")
        texto.insert("end", "ID Editorial: " + str(producto.Id_editorial) + "\n")
        texto.insert("end", "Fecha de ingreso: " + str(producto.Fechaing) + "\n")
        texto.insert("end", "Cantidades: " + str(producto.Cantidades) + "\n")
        texto.insert("end", "Tipo de producto: " + str(producto.Tipoproducto) + "\n")

        # Agrega aquí los datos adicionales de la bodega

        # Separador entre bodegas
        if i < len(productos) - 1:
            texto.insert("end", "------------------------\n")

    # Desactivar la edición del widget Text
    texto.config(state="disabled")

    # Ejecutar ventana secundaria
    ventana_mostrar.mainloop()


# Función para ingresar datos a bodega
def ingresar_datos_bodega():
    # Crear ventana secundaria para ingresar datos
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Bodega")

    # Etiquetas y campos de entrada para los datos de la bodega
    label_id = Label(ventana_ingreso, text="ID de la Bodega:")
    label_id.pack()
    entry_id = Entry(ventana_ingreso)
    entry_id.pack()

    label_nombre = Label(ventana_ingreso, text="Nombre de la Bodega:")
    label_nombre.pack()
    entry_nombre = Entry(ventana_ingreso)
    entry_nombre.pack()

    label_direccion = Label(ventana_ingreso, text="Dirección de la Bodega:")
    label_direccion.pack()
    entry_direccion = Entry(ventana_ingreso)
    entry_direccion.pack()

    label_jefe_asignado = Label(ventana_ingreso, text="Jefe Asignado de la Bodega:")
    label_jefe_asignado.pack()
    entry_jefe_asignado = Entry(ventana_ingreso)
    entry_jefe_asignado.pack()

    label_capacidad = Label(ventana_ingreso, text="Capacidad de la Bodega:")
    label_capacidad.pack()
    entry_capacidad = Entry(ventana_ingreso)
    entry_capacidad.pack()

    label_nivelocupacion = Label(ventana_ingreso, text="Nivel de ocupacion de la Bodega:")
    label_nivelocupacion.pack()
    entry_nivelocupacion = Entry(ventana_ingreso)
    entry_nivelocupacion.pack()

    label_correobodega = Label(ventana_ingreso, text="Correo de la bodega")
    label_correobodega.pack()
    entry_correobodega = Entry(ventana_ingreso)
    entry_correobodega.pack()

    label_numerofijo = Label(ventana_ingreso, text="Numero fijo de la bodega")
    label_numerofijo.pack()
    entry_numerofijo = Entry(ventana_ingreso)
    entry_numerofijo.pack()

    # Agrega aquí etiquetas y campos de entrada para los demás atributos de la bodega

    def ingresar_bodega():
        # Obtener los valores ingresados por el usuario
        id_bodega = int(entry_id.get())
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        jefe_asignado = entry_jefe_asignado.get()
        capacidad = int(entry_capacidad.get())
        nivelocupacion = int(entry_nivelocupacion.get())
        correobodega = entry_correobodega.get()
        numerofijo = entry_numerofijo.get()
        # Agrega aquí el código para obtener los demás valores ingresados por el usuario

        # Guardar la bodega
        guardar_bodega(id_bodega, nombre, direccion, jefe_asignado, capacidad, nivelocupacion, correobodega, numerofijo)

        # Cerrar la ventana de ingreso de datos
        ventana_ingreso.destroy()

    # Botón para guardar los datos ingresados
    boton_guardar = Button(ventana_ingreso, text="Guardar", command=ingresar_bodega)
    boton_guardar.pack()

    # Ejecutar ventana secundaria
    ventana_ingreso.mainloop()


# Función para ingresar datos a producto
def ingresar_datos_producto():
    # Agrega aquí el código para ingresar los datos del producto
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Producto")

    # Etiquegas y campos de entrada para los datos de producto
    label_idproducto = Label(ventana_ingreso, text="ID del Producto")
    label_idproducto.pack()
    entry_idproducto = Entry(ventana_ingreso)
    entry_idproducto.pack()

    label_ideditorial = Label(ventana_ingreso, text="ID de la editorial")
    label_ideditorial.pack()
    entry_ideditorial = Entry(ventana_ingreso)
    entry_ideditorial.pack()

    label_cantidades= Label(ventana_ingreso, text="Cantidades de los productos")
    label_cantidades.pack()
    entry_cantidades= Entry(ventana_ingreso)
    entry_cantidades.pack()

    label_tipoproducto= Label(ventana_ingreso, text="Tipo de producto")
    label_tipoproducto.pack()
    entry_tipoproducto= Entry(ventana_ingreso)
    entry_tipoproducto.pack()

    def ingresar_producto():
        id_producto = int(entry_idproducto.get())
        id_editorial = int(entry_ideditorial.get())
        fechaing = datetime.now()
        cantidades = int(entry_cantidades.get())
        tipoproducto = str(entry_tipoproducto.get())

        guardar_producto(id_producto,id_editorial,fechaing,cantidades,tipoproducto)

        ventana_ingreso.destroy()

    boton_guardar = Button(ventana_ingreso, text="Guardar", command=ingresar_producto)
    boton_guardar.pack()

# Función para actualizar bodega
def solicitar_datos_actualizacion_bodega():
    # Agrega aquí el código para solicitar los datos de actualización de la bodega
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Producto")

    label_idbodega = Label(ventana_ingreso, text="ID de la bodega")
    label_idbodega.pack()
    entry_idbodega = Entry(ventana_ingreso)
    entry_idbodega.pack()

    label_campoactualizar= Label(ventana_ingreso, text="Campo que desea actualizar")
    label_campoactualizar.pack()
    entry_campoactualizar= Entry(ventana_ingreso)
    entry_campoactualizar.pack()

    label_nuevovalor= Label(ventana_ingreso, text="Nuevo valor")
    label_nuevovalor.pack()
    entry_nuevovalor= Entry(ventana_ingreso)
    entry_nuevovalor.pack()
    def actualizacion_bodega():
        id_bodega = int(entry_idbodega.get())
        campoactualizar = str(entry_campoactualizar.get())
        nuevovalor = str(entry_nuevovalor.get())

        actualizar_bodega(id_bodega,campoactualizar,nuevovalor)
        ventana_ingreso.destroy()

    boton_guardar = Button(ventana_ingreso, text="Actualizar", command=actualizacion_bodega)
    boton_guardar.pack()



# Función para actualizar producto
def solicitar_datos_actualizacion_producto():
    # Agrega aquí el código para solicitar los datos de actualización de la bodega
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Producto")

    label_idproducto = Label(ventana_ingreso, text="ID del Producto")
    label_idproducto.pack()
    entry_idproducto = Entry(ventana_ingreso)
    entry_idproducto.pack()

    label_campoactualizar= Label(ventana_ingreso, text="Campo que desea actualizar")
    label_campoactualizar.pack()
    entry_campoactualizar= Entry(ventana_ingreso)
    entry_campoactualizar.pack()

    label_nuevovalor= Label(ventana_ingreso, text="Nuevo valor")
    label_nuevovalor.pack()
    entry_nuevovalor= Entry(ventana_ingreso)
    entry_nuevovalor.pack()
    def actualizacion_producto():
        id_producto = int(entry_idproducto.get())
        campoactualizar = str(entry_campoactualizar.get())
        nuevovalor = str(entry_nuevovalor.get())

        actualizar_producto(id_producto,campoactualizar,nuevovalor)
        ventana_ingreso.destroy()

    boton_guardar = Button(ventana_ingreso, text="Actualizar", command=actualizacion_producto)
    boton_guardar.pack()



# Función para eliminar bodega
def dato_eliminar_bodega():
    pass
    # Agrega aquí el código para eliminar una bodega


# Función para eliminar producto
def dato_eliminar_producto():
    pass
    # Agrega aquí el código para eliminar un producto


# Crear ventana principal
ventana = Tk()
ventana.title("Programa de El loco")
ventana.geometry("1000x300")


marco_botones = Frame(ventana)
marco_botones.pack(pady=10)

# Etiqueta de título
titulo = Label(ventana, text="Programa de El loco", font=("Arial", 20))
titulo.pack(pady=10)

# Botones
boton_mostrar_bodega = Button(ventana, text="Mostrar Bodega", command=mostrar_bodega)
boton_mostrar_bodega.pack(side="left", padx=10)

boton_mostrar_producto = Button(ventana, text="Mostrar Producto", command=mostrar_producto)
boton_mostrar_producto.pack(side="left", padx=10)

boton_ingresar_bodega = Button(ventana, text="Ingresar Bodega", command=ingresar_datos_bodega)
boton_ingresar_bodega.pack(side="left", padx=10)

boton_ingresar_producto = Button(ventana, text="Ingresar Producto", command=ingresar_datos_producto)
boton_ingresar_producto.pack(side="left", padx=10)

boton_actualizar_bodega = Button(ventana, text="Actualizar Bodega", command=solicitar_datos_actualizacion_bodega)
boton_actualizar_bodega.pack(side="left", padx=10)

boton_actualizar_producto = Button(ventana, text="Actualizar Producto", command=solicitar_datos_actualizacion_producto)
boton_actualizar_producto.pack(side="left", padx=10)

boton_eliminar_bodega = Button(ventana, text="Eliminar Bodega", command=dato_eliminar_bodega)
boton_eliminar_bodega.pack(side="left", padx=10)

boton_eliminar_producto = Button(ventana, text="Eliminar Producto", command=dato_eliminar_producto)
boton_eliminar_producto.pack(side="left", padx=10)

# Ejecutar ventana
ventana.mainloop()
