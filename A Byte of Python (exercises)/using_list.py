shoplist=['apples','mango','carrot','bananas']

print('I have to shop: ', len(shoplist))

print ('Purchase:')
for item in shoplist:
    print(item, end=' ')

print('\nAlso need to by rice.')
shoplist.append('rice')
print('Now the shopList is: ',shoplist)

print('Sort our list.')
shoplist.sort()
print('SortedList: ',shoplist)

