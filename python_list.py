# list1 = [1, 2, 3, 4, 5]


# print(list1, sep = " ")

# # list1.insert(len(list1), 6) asi no 
# #es asi 
# # list1.append(6)
# # incrementar
# # list1.extend([(6, 7, 8, 9)])
# #list1.pop(4)

# for x in list1:
#     print('value ', x)

#-------------------------------------------------------#
#haga un programa que muestre la lsita de productos de un supermercado y refleje el precio

lista_productos = {
    'manzana': 5.2,
    'jabon de plato': 4.7,
    'coco': 3.8,
    'electrodomesticos': 34.9,
    'banana': 11.0,
    'cafe': 22.0,
}

print('lista de los productos del supermercado y sus precios: ')
for producto, precio in lista_productos.items():
    print(f'{producto.capitalize()}: ${precio:2f}')