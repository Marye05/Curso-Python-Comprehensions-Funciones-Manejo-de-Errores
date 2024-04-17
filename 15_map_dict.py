items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(items) # aca imprime la lista oiginal no cambia nada
print(prices) # [100, 300, 200]

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items) 
'''
[
  {
    'product': 'camisa',
    'price': 100,
    'taxes': 19.0
  },
  {
    'product': 'pantalones',
    'price': 300,
    'taxes': 57.0
  },
  {
    'product': 'pantalones 2',
    'price': 200,
    'taxes': 38.0
  }
]
'''
print(items)