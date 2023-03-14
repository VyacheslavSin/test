user = 'Python'.upper()
c = 'privet {name}!'.format(name = user)
print(c)

c = f'PRIVET {user}'.lower()
print(c)

c = f'PRIVET {user}'.capitalize()
print(c)

c = '      PR I V ET      '
b = c.strip()
d = c.replace(' ', '')
e = ' привет т3б3!     '.replace('3', 'е').strip().capitalize()
print(c)
print(b)
print(d)
print(e)


a = 'learn   python   so  fucking Python'
b = a.split()
print(b)
print(len(b))
print(type(a))


