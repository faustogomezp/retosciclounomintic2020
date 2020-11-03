def calcularDescuento(valor_compra):
    if valor_compra > 150000 and valor_compra <= 300000:
        porcentaje_descuento = 0.1
    elif valor_compra > 300000 and valor_compra <= 700000:
        porcentaje_descuento = 0.15
    else:
        porcentaje_descuento = 0.2
    return valor_compra * porcentaje_descuento


def registrarProductos():
    cant_productos = int(input())
    costo_total = 0
    costo_producto=0
    productos = []
    valores = []
    i = 0
    for i in range(i, cant_productos):
        productos.append(input())
        costo_producto = int(input())
        valores.append(costo_producto)
        costo_total += costo_producto

    return productos, valores, costo_total
        

def impresionTirilla(productos):
    costo_total = productos[2]
    print('Centro Comercial Unaleño')
    print('Compra más y Gasta Menos')
    print('NIT: 899.999.063')
    i = 0
    valores = productos[1]
    for producto in productos[0]:
        print(f'{producto} ${valores[i]}')
        i +=1

    if costo_total <= 150000:
        descuento = 0
    else:
        descuento = int(calcularDescuento(costo_total))
        costo_total = costo_total - descuento
    print(f'Total: ${costo_total}')
    print(f'En esta compra tu descuento fue ${descuento}')
    print('Gracias por tu compra')


if __name__ == "__main__":
    impresionTirilla(registrarProductos())