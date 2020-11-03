import math

def calcularDescuento(valor_compra):
    if valor_compra > 150000 and valor_compra <= 300000:
        porcentaje_descuento = 0.1
    elif valor_compra > 300000 and valor_compra <= 700000:
        porcentaje_descuento = 0.15
    else:
        porcentaje_descuento = 0.2
    return valor_compra * porcentaje_descuento

def registrarProductos(comando):
    opcion, producto, cant ,costo_producto = comando.split('&')
    costo_total=int(cant) * int(costo_producto)
    return producto, cant, costo_total
        

def impresionTirilla(productos, comando):
    valor_compra = 0
    cliente = comando.split('&')[1]
    print('Centro Comercial Unaleño')
    print('Compra más y Gasta Menos')
    print('NIT: 899.999.063')
    print(f'Cliente: {cliente}')
    print('Art Cant Precio')
    for producto in productos:
        print(f'{producto[0]} x{producto[1]} ${producto[2]}')
        valor_compra = valor_compra + producto[2]
    if valor_compra <= 150000:
        descuento = 0
    else:
        descuento = float(calcularDescuento(valor_compra))
        valor_compra = valor_compra - descuento
    print(f'Total: ${math.ceil(valor_compra)}')
    print(f'En esta compra tu descuento fue ${int(descuento)}')
    print('Gracias por tu compra')
    print('---')


if __name__ == "__main__":
    comando = input()
    lista_productos = []
    while comando != '3':
        if comando.split('&')[0] == '1':
            lista_productos.append(registrarProductos(comando))
        elif comando.split('&')[0] == '2':
            impresionTirilla(lista_productos, comando)
            lista_productos = []
        comando = input()
        """ impresionTirilla() """