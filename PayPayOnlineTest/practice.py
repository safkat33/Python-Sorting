import random

array = [2, 3, 4, 6, 7, 8, 9, 2, 1, 10]

python_dict = {'one': 'licence', 'two': 'buy', 'three': 'car'}
print(python_dict)

dict_key = list(python_dict.keys())
print(dict_key)

dict_values = python_dict.keys()
print(i for i in dict_values)
for i in dict_values:
    print(i)

for key, value in python_dict.items():
    print(key, value)

print('Random Number in a range(2,8)=>', random.randint(2, 8))
