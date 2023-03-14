phone = ['iPhone Xs', 'Samsung 10s', 'Xiaomi Mi8']
print(phone)
print(len(phone))

phone.append('Motorola')
print(phone)

print(phone.count('Samsung 10s'))

print(phone[0])
print(phone[1:3])


print(phone[-1])

print(phone.index('Motorola'))

phone.sort()
print(phone)

print('Motorola' in phone)

phone.append('Huy')
print(phone)

del phone[4]
print(phone)

phone.remove('Motorola')
print(phone)
