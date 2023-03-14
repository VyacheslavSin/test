phone = ['iPhone Xs', 'Samsung 10s', 'Xiaomi Mi8']


product = {
    'name': "Motorola",
    'stock': 5,
    'price': 65000.0 
}
print(product)
print(len(product))

product['memory'] = 64
print(product)

product['name'] = 'iPhone 13Pro'
print(product)

print(product.get('discount', 0))

del product['memory']

print(product)
product['recommend'] = phone

print(product)
print(product['recommend'])
print(product['recommend'][1])

product['recommend'].append('huy')
print(product['recommend'])

# могут быть словари в списках и списки в словарях
