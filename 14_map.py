numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers) # [1, 2, 3, 4]
print(numbers_v2) # [2, 4, 6, 8]
print(numbers_v3) # [2, 4, 6, 8]

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1) # [1, 2, 3, 4]
print(numbers_2) # [5, 6, 7]
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result) # [6, 8, 10]