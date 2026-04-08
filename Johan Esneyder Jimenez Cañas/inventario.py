def mostrar_inventario(productos):
    print("mostrar inventario")
    if not productos:
        print("No hay productos registrados")
        return
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")

def agregar_producto(productos, nombre, precio):
    if isinstance(nombre, str) and nombre.strip() and isinstance(precio, (int, float)) and precio >= 0:
        productos.append({"nombre": nombre.title(), "precio": precio})
        print(f"Producto '{nombre.title()}' agregado")
    else:
        print("Producto no agregado, datos invalidos, el valor debe ser número positivo")

def insertar_producto(productos, indice, nombre, precio):
    if 0 <= indice <= len(productos) and isinstance(precio, (int, float)) and precio > 0:
        productos.insert(indice, {"nombre":nombre.title(), "precio": precio})
        print(f"Producto '{nombre.title()}' insertado en posicion {indice + 1}.")
    else:
        print("Indice o precio invalido")

if __name__ == "__main__":
    #inventario inicial
    inventario = [
        {"nombre": "Taladro", "precio": 12345},
        {"nombre": "Martillo", "precio": 45678},
        {"nombre": "Destornillador", "precio": 1234567345},
    ]
    #mostrar inventario
    mostrar_inventario(inventario)

    print("-----------------------------------------------")

    agregar_producto(inventario, "Sierra Circular", 2345678)
    mostrar_inventario
    
   