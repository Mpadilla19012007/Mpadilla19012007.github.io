
import tkinter as tk
from tkinter import messagebox

# Productos del catalogo
productos = [
    {
        "nombre": "Labial Mate",
        "categoria": "Maquillaje",
        "precio": 18000,
        "descripcion": "Labial de larga duracion con acabado mate."
    },
    {
        "nombre": "Pestanina",
        "categoria": "Maquillaje",
        "precio": 22000,
        "descripcion": "Realza tus pestanas y aporta volumen."
    },
    {
        "nombre": "Rubor Rosado",
        "categoria": "Maquillaje",
        "precio": 25000,
        "descripcion": "Rubor para darle color natural a tus mejillas."
    },
    {
        "nombre": "Base Liquida",
        "categoria": "Maquillaje",
        "precio": 45000,
        "descripcion": "Base para unificar el tono de la piel."
    },
    {
        "nombre": "Polvo Compacto",
        "categoria": "Maquillaje",
        "precio": 30000,
        "descripcion": "Ayuda a controlar el brillo del rostro."
    },
    {
        "nombre": "Agua Micelar",
        "categoria": "Limpieza facial",
        "precio": 20000,
        "descripcion": "Ayuda a retirar maquillaje e impurezas."
    },
    {
        "nombre": "Gel Limpiador Facial",
        "categoria": "Limpieza facial",
        "precio": 28000,
        "descripcion": "Limpia el rostro y elimina residuos."
    },
    {
        "nombre": "Tonico Facial",
        "categoria": "Limpieza facial",
        "precio": 24000,
        "descripcion": "Complementa la limpieza del rostro."
    },
    {
        "nombre": "Exfoliante Facial",
        "categoria": "Limpieza facial",
        "precio": 32000,
        "descripcion": "Ayuda a eliminar celulas muertas."
    },
    {
        "nombre": "Crema Hidratante",
        "categoria": "Limpieza facial",
        "precio": 35000,
        "descripcion": "Hidrata la piel y ayuda a mantenerla suave."
    }
]

# Ventana principal
ventana = tk.Tk()
ventana.title("Belleza y Skincare")
ventana.geometry("750x600")
ventana.configure(bg="#FCE4EC")

# Titulo
titulo = tk.Label(
    ventana,
    text="CATALOGO DE BELLEZA",
    font=("Arial", 22, "bold"),
    bg="#FCE4EC",
    fg="#AD1457"
)
titulo.pack(pady=15)

subtitulo = tk.Label(
    ventana,
    text="Maquillaje y cuidado de tu piel",
    font=("Arial", 12),
    bg="#FCE4EC",
    fg="#880E4F"
)
subtitulo.pack()

# Busqueda
entrada = tk.Entry(ventana, font=("Arial", 12), width=35)
entrada.pack(pady=12)
entrada.insert(0, "Buscar producto...")

# Lista de productos
lista = tk.Listbox(
    ventana,
    font=("Arial", 12),
    width=65,
    height=15,
    bg="white",
    fg="#880E4F",
    selectbackground="#F48FB1"
)
lista.pack(pady=10)


def mostrar_productos(categoria="Todos"):
    lista.delete(0, tk.END)

    for producto in productos:
        if categoria == "Todos" or producto["categoria"] == categoria:
            lista.insert(
                tk.END,
                producto["nombre"] + " - $"
                + format(producto["precio"], ",").replace(",", ".")
                + " - " + producto["categoria"]
            )


def buscar_producto():
    texto = entrada.get().lower()
    lista.delete(0, tk.END)

    for producto in productos:
        if texto in producto["nombre"].lower():
            lista.insert(
                tk.END,
                producto["nombre"] + " - $"
                + format(producto["precio"], ",").replace(",", ".")
                + " - " + producto["categoria"]
            )


def ver_detalles():
    seleccion = lista.curselection()

    if not seleccion:
        messagebox.showwarning(
            "Atencion", "Selecciona un producto primero."
        )
        return

    nombre_lista = lista.get(seleccion[0]).split(" - $")[0]

    for producto in productos:
        if producto["nombre"] == nombre_lista:
            mensaje = (
                "Producto: " + producto["nombre"] + "\n"
                + "Categoria: " + producto["categoria"] + "\n"
                + "Precio: $" + format(producto["precio"], ",")
                .replace(",", ".") + " COP\n\n"
                + producto["descripcion"]
            )

            messagebox.showinfo("Detalles del producto", mensaje)
            break


# Botones de categorias
frame = tk.Frame(ventana, bg="#FCE4EC")
frame.pack(pady=5)

tk.Button(
    frame, text="Todos",
    command=lambda: mostrar_productos("Todos"),
    bg="#EC407A", fg="white", width=14
).grid(row=0, column=0, padx=5)

tk.Button(
    frame, text="Maquillaje",
    command=lambda: mostrar_productos("Maquillaje"),
    bg="#EC407A", fg="white", width=14
).grid(row=0, column=1, padx=5)

tk.Button(
    frame, text="Limpieza facial",
    command=lambda: mostrar_productos("Limpieza facial"),
    bg="#EC407A", fg="white", width=14
).grid(row=0, column=2, padx=5)

# Botones adicionales
tk.Button(
    ventana,
    text="Buscar",
    command=buscar_producto,
    bg="#AD1457",
    fg="white",
    width=20
).pack(pady=5)

tk.Button(
    ventana,
    text="Ver detalles del producto",
    command=ver_detalles,
    bg="#880E4F",
    fg="white",
    width=25
).pack(pady=5)

# Mostrar productos al iniciar
mostrar_productos()

# Ejecutar programa
ventana.mainloop()
