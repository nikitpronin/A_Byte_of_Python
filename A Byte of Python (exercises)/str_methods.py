name='Swaroop'# Это объект строки
if name.startswith('Swa'):
    print('Да, строка начинается на "Swa" ')

if'a' in name:
    print('Да, она содержит строку "a"')

if name.find('war')!= -1:
    print('Да, она содержит строку "war"')

delimiter='_*_'

mylist = ['Brazil','Russia','India', 'China']

print(delimiter.join(mylist))
