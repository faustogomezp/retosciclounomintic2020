import math
import json
import requests


#Función para leer los archivos json.
def leerJSON(url):
    resp = requests.get(url)
    return json.loads(resp.text)

#Función para calcular los descuentos de acuerdo al valor de la compra.
def calcularDescuento(valor_compra):
    if valor_compra > 150000 and valor_compra <= 300000:
        porcentaje_descuento = 0.1
    elif valor_compra > 300000 and valor_compra <= 700000:
        porcentaje_descuento = 0.15
    else:
        porcentaje_descuento = 0.2
    return valor_compra * porcentaje_descuento

""" def registrarProductos(comando):
    opcion, producto, cant ,costo_producto = comando.split('&')
    costo_total=int(cant) * int(costo_producto)
    return producto, cant, costo_total """
        
#Función para imprimir la tirilla recibiendo como parametro un diccionario.
def impresionTirilla(tirillas):
    #Ciclo para iterar las tirillas, la cual tiene dos Llaves, una con el nombre del cliente y la otra con los productos comprados.
    for tirilla in tirillas:
        valor_compra = 0
        #Obtenemos el nombre del cliente con la llave.
        cliente = tirilla['cliente']
        print('Centro Comercial Unaleño')
        print('Compra más y Gasta Menos')
        print('NIT: 899.999.063')
        print(f'Cliente: {cliente}')
        print('Art Cant Precio')
        #Ciclo para iterar los productos con la llava produtos.
        for producto in tirilla['productos']:
            nombre_producto = producto['nombre']
            cantidad = int(producto['cantidad'])
            precio_total = cantidad * int(producto['precio unitario'])
            print(f'{nombre_producto} x{cantidad} ${precio_total}')
            valor_compra = valor_compra + precio_total
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
    dir_json = input()
    tirillas = leerJSON(dir_json)
    print(tirillas)
    impresionTirilla(tirillas)
    """comando = input()
    lista_productos = []
    while comando != '3':
        if comando.split('&')[0] == '1':
            lista_productos.append(registrarProductos(comando))
        elif comando.split('&')[0] == '2':
            impresionTirilla(lista_productos, comando)
            lista_productos = []
        comando = input() """

    
