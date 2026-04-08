def agregar_producto(inventario, nombre):
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        inventario.append(nombre.title())
        print(f"Producto registrado: {nombre.title()}")
    else:
        print("Error: El nombre debe tener entre 2 y 50 caracteres.")

def mostrar_inventario(inventario):
    for producto in inventario:
        print(f"- {producto}")

def modificar_producto(inventario, indice, nuevo_nombre):
    if isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        if 0 <= indice < len(inventario):
            original = inventario[indice]
            inventario[indice] = nuevo_nombre.title()
            print(f"Actualizado: {original} -> {nuevo_nombre.title()}")
        else:
            print("Error: Índice de producto no encontrado.")
    else:
        print("Error: El nuevo nombre no es válido.")

def eliminar_producto(inventario, indice):
    if 0 <= indice < len(inventario):
        eliminado = inventario.pop(indice)
        print(f"Producto retirado: {eliminado}")
    else:
        print("Error: No se pudo eliminar. Índice fuera de rango.")

def contar_existencias(inventario):
    print(f"Total de referencias en inventario: {len(inventario)}")

def listar_alfabeticamente(inventario):
    for producto in sorted(inventario):
        print(producto)

def main():
    productos = ["Arroz", "Café", "Panela"]
    
    print("--- Inventario Inicial ---")
    mostrar_inventario(productos)
    
    print("\n--- Registro de Mercancía ---")
    agregar_producto(productos, "Leche")
    mostrar_inventario(productos)
    
    print("\n--- Ajuste de Inventario ---")
    modificar_producto(productos, 1, "Chocolate")
    mostrar_inventario(productos)
    
    print("\n--- Baja de Producto ---")
    eliminar_producto(productos, 0)
    mostrar_inventario(productos)

if __name__ == "__main__":
    main()