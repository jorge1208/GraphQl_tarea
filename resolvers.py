# resolvers.py

# Base de datos simulada de productos
productos_db = {
    "1": {"id": "1", "nombre": "Camiseta", "precio": 20},
    "2": {"id": "2", "nombre": "Pantalones", "precio": 40},
}

# Resolver para la consulta "producto"
def resolve_producto(obj, info, id):
    return productos_db.get(id)

# Resolver para la mutación "actualizarPrecio"
def resolve_actualizar_precio(obj, info, id, precio):
    producto = productos_db.get(id)
    if producto:
        producto["precio"] = precio
        return producto
    return None
