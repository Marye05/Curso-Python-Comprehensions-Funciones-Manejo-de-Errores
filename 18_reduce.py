import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter) # 1
  print('item => ',item) # 2
  return counter + item

result = functools.reduce(accum, numbers)

print(result) # 10